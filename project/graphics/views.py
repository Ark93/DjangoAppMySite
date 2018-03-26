from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from transactions.models import Transaccion
import plotly.offline as opy
import plotly.graph_objs as go

#https://matplotlib.org/faq/howto_faq.html#matplotlib-in-a-web-application-server
#https://mpld3.github.io/quickstart.html
#https://stackoverflow.com/questions/10944621/dynamically-updating-plot-in-matplotlib
#https://stackoverflow.com/questions/35092571/how-to-create-charts-with-plotly-on-django

##Time series https://plot.ly/pandas/time-series/#basic-time-series
class Graph(generic.TemplateView):
    template_name = 'graphics/graphic.html'
    def get_context_data(self, **kwargs):
        context = super(Graph, self).get_context_data(**kwargs)
        data_ = Transaccion.objects.order_by('fecha')
        
        gastos_y_ax = [(t.cargo  + t.abono) for t in data_]
        fechas_x_ax = [t.fecha for t in data_]
        
        gastos = go.Scatter(x=fechas_x_ax, y= gastos_y_ax, marker={'color': 'red', 'symbol': 0, 'size': "10"},
                            mode="markers",  name='Gastos')
        data = go.Data([gastos])
        layout=go.Layout(title="Todos los Gastos", xaxis={'title':'Fecha'}, yaxis={'title':'Gasto'}, hovermode = 'closest')
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=True, output_type='div')

        context['graph'] = div

        return context