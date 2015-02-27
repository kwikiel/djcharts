from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from demoapp.views import LineChartView, DonutChartView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^line', LineChartView.as_view(), name="line_view"),
    url(r'^donut', DonutChartView.as_view(), name="donut_view"),
    url(r'^$', TemplateView.as_view(template_name='index.html'))
)
