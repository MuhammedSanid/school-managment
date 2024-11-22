from django.urls import path
from new import views

urlpatterns = [
    path('',views.index,name='index'),
    path('logins',views.logins,name='logins'),
    path('Student_registration',views.Student_registration,name='Student_registration'),
    path('Teacher_registration',views.Teacher_registration,name='Teacher_registration'),
    path('view_student',views.view_student,name='view_student'),
    path('view_teacher',views.view_teacher,name='view_teacher'),
    path('delete_student/<int:id>',views.delete_student,name='delete_student'),
    path('delete_teacher/<int:id>',views.delete_teacher,name='delete_teacher'),
    path('edit_student/<int:id>',views.edit_student,name="edit_student"),
    path('upd_student/<int:id>,<int:idd>',views.upd_student,name="upd_student"),
    path('edit_teacher/<int:id>',views.edit_teacher,name="edit_teacher"),
    path('upd_teacher/<int:id>,<int:idd>',views.upd_teacher,name="upd_teacher"),
    path('st_home',views.st_home,name='st_home'),
    path('vw_st',views.vw_st,name="vw_st"),
    path('vw_tcr',views.vw_tcr,name='vw_tcr'),
    path('update_stud/<int:id>,<int:idd>',views.update_stud,name='update_stud'),
    path('approve',views.approve,name="approve"),
    path('aprvd/<int:id>',views.aprvd,name="aprvd"),
    path('edit_stud/<int:id>',views.edit_stud,name='edit_stud'),
    path('edit_tcr/<int:id>',views.edit_tcr,name='edit_tcr'),
    path('update_tcr/<int:id>,<int:idd>',views.update_tcr,name='update_tcr'),
    path('tc_home',views.tc_home,name='tc_home'),
]
