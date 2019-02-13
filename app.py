"""
Author: Jiri Volprecht
"""

from flask import Flask, render_template, request, send_file
from file_analyzer import FileAnalyzer
from webmap import Webmap
from scripts import clean, count_temp_files
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    tmp_files = count_temp_files()
    return render_template("index.html", cnt_tmp=tmp_files)


@app.route("/success", methods=["POST"])
def success():
    global file_a, webmap
    tmp_files = count_temp_files()
    if request.method == "POST" and "file" in request.files:
        file = request.files["file"]
        print(file)
        file_a = FileAnalyzer(file)
        if file_a.validate_columns():
            file_a.get_position()
            webmap = Webmap(file_a.df)
            webmap.create_webmap()
            filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f" + ".html")
            webmap.save_map(filename)
            return render_template("success.html",
                                   btn="download.html",
                                   tables=[
                                       file_a.df.to_html(
                                           classes='data table table-sm table-hover center',
                                           header="true"
                                       )
                                   ])
        else:
            return render_template(
                "index.html",
                cnt_tmp=tmp_files,
                message="Column 'address' or 'Address' is not present"
            )
    else:
        return render_template(
            "index.html",
            cnt_tmp=tmp_files,
            message="No file chosen. Please try to choose a csv file first."
        )


@app.route("/download-file")
def download_file():
    return send_file(
        file_a.filename,
        attachment_filename="modified_file.csv",
        as_attachment=True
    )


@app.route("/download-map")
def download_map():
    return send_file(
        f"templates/{webmap.filepath}",
        attachment_filename="map.html",
        as_attachment=True
    )


@app.route("/show-map")
def show_map():
    return render_template(webmap.filepath)


@app.route("/clear-temp")
def clear_temp():
    clean()
    tmp_files = count_temp_files()
    return render_template(
        "index.html",
        message="Temporary files were deleted.",
        cnt_tmp=tmp_files
    )


if __name__ == '__main__':
    app.debug = True
    app.run()
