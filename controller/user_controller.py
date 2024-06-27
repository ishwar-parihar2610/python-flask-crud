#This is our controller

from app import appmain
from flask import request,send_file
from model.user_model import user_model
from datetime import datetime

obj=user_model()
@appmain.route('/user/getall')
def signUp():
    return obj.user_getall_model() 

@appmain.route('/user/addone',methods=['POST'])
def user_addone_controller():
   return  obj.user_addone_model(request.form)

@appmain.route('/user/update', methods=['PUT'])
def user_update_controller():
    return obj.user_update_model(request.form)

@appmain.route('/user/delete/<int:id>', methods=['DELETE'])
def user_delete_controller(id):
    return obj.user_delete_controller(id)


@appmain.route('/user/patch/<int:id>', methods=['PATCH'])
def user_patch_controller(id):
   
    return obj.user_patch_model(request.form,id)

@appmain.route("/user/<uid>/upload/avatar",methods=['PUT'])
def user_upload_avtar_controller(uid):
    file= request.files['avatar']
    
    uniqueFileName= str(datetime.now().timestamp()).replace(".","") 
    fileNameSplit=file.filename.split(".")
    ext= fileNameSplit[len(fileNameSplit)-1]
    finalFilePath=f"upload/{uniqueFileName}.{ext}"
    file.save(f"upload/{uniqueFileName}.{ext}")
    return obj.user_upload_avatar_model(uid,finalFilePath)

    # return str(file.filename).split(".")
@appmain.route("/uploads/<filename>", methods=['GET'])
def user_get_avatar_controller(filename):

    return send_file(f"upload/{filename}")
