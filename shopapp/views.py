from django.views.generic import TemplateView 
from django.shortcuts import HttpResponseRedirect, HttpResponse
from shopapp import models as shop_models
from authapp import models as auth_models


class Items(TemplateView):
    template_name = "shopapp/shop.html"

    def get_context_data(self, **kwargs):
        context = super(Items, self).get_context_data(**kwargs)
        context['shop_items'] = shop_models.ShopItemsModel.objects.all()
        context['user_items'] = []
        user_items = shop_models.UserItemsModel.objects.filter(user=self.request.user)
        for item in user_items:
            context['user_items'].append(item.item)
        return context
    
    def get(self, request, *args, **kwargs):
        if request.GET.get('buy'):
            buy_id = request.GET.get('buy')
            buy_item = shop_models.ShopItemsModel.objects.get(id=buy_id)
            if request.user.balance >= buy_item.price:
                request.user.balance -= buy_item.price
                request.user.save()
                user_item = shop_models.UserItemsModel.objects.create(item=buy_item, user=request.user, type=buy_item.type, color=buy_item.color)
                user_item.save()
            return HttpResponseRedirect("/shop/user_items/")
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
class UserItems(TemplateView):
    template_name = "shopapp/user_items.html"

    def get_context_data(self, **kwargs):
        context = super(UserItems, self).get_context_data(**kwargs)
        context['user_items'] = shop_models.UserItemsModel.objects.filter(user=self.request.user)
        return context
    
    def get(self, request, *args, **kwargs):
        if request.GET.get('activate'):
            activate_id = request.GET.get('activate')
            item = shop_models.UserItemsModel.objects.get(id=activate_id)
            if item.type == "BORDER":
                request.user.border_color = item.color
            else: 
                request.user.profile_background = item.color
            request.user.save()
            return HttpResponseRedirect("/shop/user_items/")
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    