from django.views.generic import TemplateView

from .models import Film


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['sexta'] = Film.objects.get_today_films_by_channel_order_by_hour('Sexta')
        context['sexta3'] = Film.objects.get_today_films_by_channel_order_by_hour('Sexta 3')
        context['nova'] = Film.objects.get_today_films_by_channel_order_by_hour('Nova')
        context['nitro'] = Film.objects.get_today_films_by_channel_order_by_hour('Nitro')
        context['neox'] = Film.objects.get_today_films_by_channel_order_by_hour('Neox')
        context['antena3'] = Film.objects.get_today_films_by_channel_order_by_hour('Antena 3')
        return context
