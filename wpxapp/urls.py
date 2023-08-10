from django.urls import path
from . import views
# from django.conf.urls import url
from django.urls import re_path as url

urlpatterns = [
    path('', views.home, name='wpx-home'),
    path('about/', views.about, name='wpx-about'),
    url(r'^bookings_status/$', views.bookings_status, name='bookings_status'),
    url(r'^sendemail/$', views.sendemail, name='sendemail'),
    url(r'^sendemail_other/$', views.sendemail_other, name='sendemail_other'),
    url(r'^sendemailpending/$', views.sendemailpending, name='sendemailpending'),
    url(r'^sendemailreceipt/$', views.sendemailreceipt, name='sendemailreceipt'),
    url(r'^sendegeneralemail/$', views.sendegeneralemail, name='sendegeneralemail'),
    url(r'^fix_data/$', views.fix_data, name='fix_data'),
    url(r'^send_received_message_email/$', views.send_received_message_email, name='send_received_message_email'),
    path('registered_users/', views.registered_users, name='registered_users'),
    path('bad_data/', views.bad_data,  name='bad_data'),
    path('unread_messages/', views.display_unread_messages,  name='unread_messages'),
]