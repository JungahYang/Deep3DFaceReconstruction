from flask import request, Response, render_template, send_file, after_this_request, json, jsonify, send_from_directory
import os, json, glob, io
from PIL import Image
import zipfile

from app import app
from app.service import NotAcceptableException
from app.utils import SafeUtils

import subprocess

@app.route("/")
def index():
	return render_template("test.html")


@app.route('/result', methods = ['POST'])
def result():
	try:
		return_data = io.BytesIO()
		uploaded_files = request.files.getlist('files[]')
		if len(uploaded_files) == 0:
			uploaded_files = request.files.getlist('file')

		
		input_img = Image.open(uploaded_files[0])
		fname = uploaded_files[0].filename.split('.')[0]
		if uploaded_files[0].filename.split('.')[-1] == "jpg":
			fpath = "/mnt/DATA/yg/uniinfo/3DDFA_V2/examples/inputs/"+fname+".jpg"
		elif uploaded_files[0].filename.split('.')[-1] == "png":
			fpath = "/mnt/DATA/yg/uniinfo/3DDFA_V2/examples/inputs/"+fname+".png"
		else:
			raise Exception("jpg 또는 png 파일만 가능합니다.")

		input_img.save(fpath)
		r1 = os.popen("python /mnt/DATA/yg/uniinfo/3DDFA_V2/demo.py -f "+fpath+" -o obj").read()
		os.system("python /mnt/DATA/yg/uniinfo/3DDFA_V2/demo.py -f "+fpath+" -o uv_tex")
		print(r1)
		if "0 faces" in r1:
			raise Exception("얼굴을 찾을 수 없습니다.")
		os.system("mv /mnt/DATA/yg/uniinfo/3DDFA_V2/examples/results/"+fname+"_* ./")
		os.system("zip result.zip "+fname+"_*")
		os.system("rm "+fname+"_*")
		
		with open("result.zip", 'rb') as output:
			return_data.write(output.read())
			return_data.seek(0)

		os.remove("result.zip")
		
		return send_file(
			return_data,
			mimetype="application/zip",
			attachment_filename=fname+"_result.zip",
			as_attachment=True)

	except Exception as e:
		# print traceback on debug level below
		if app.logger.level <= 10: app.logger.exception(e)
		error = str(e).replace("&", "&amp;").replace("\"", "\'").replace(">", "&gt;").replace("<", "&lt;")
		error = "<html><body><script>alert(\"{}\");window.history.back();</script></html>".format(error)

		return app.make_response(error)