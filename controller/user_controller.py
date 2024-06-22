#This is our controller

from app import appmain
from flask import request
from model.user_model import user_model

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



