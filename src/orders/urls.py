from django.urls import path
from orders import views


app_name = 'orders'

urlpatterns = [
    path('create-order/', views.CreateOrderView.as_view(), name='create-order'),
    path('view-orders/', views.ListOrdersView.as_view(), name='view-orders'),
    path('update-status-order/', views.SendOrderStatusView.as_view(), name='update-status-order'),
    path('detail-order/<int:pk>', views.DetailOrderView.as_view(), name='detail-order'),
    path('update-order/<int:pk>', views.UpdateOrderView.as_view(), name='update-order'),
    path('cancel-order/<int:pk>', views.CancelOrderView.as_view(), name='cancel-order'),
    path('update-order-cart/', views.UpdateOrderCartView.as_view(), name='update-order-cart'),
    path('send-comment/', views.SendOrderCommentView.as_view(), name='send-comment'),

]
