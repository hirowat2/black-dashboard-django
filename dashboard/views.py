from django.shortcuts import render
from fasthtml import common as fh


def create_chart_component():
    chart_div = fh.Div(
        fh.H2("Gráfico de Vendas"),
        fh.Div("Gráfico aqui...", class_name="chart-content"),
        class_name="chart"
    )
    return chart_div

def create_stats_component():
    stats_div = fh.Div(
        fh.H2("Estatísticas"),
        fh.P("Total de Usuários: 1200"),
        fh.P("Média de Vendas: $5600"),
        class_name="stats"
    )
    return stats_div

def dashboard_view(request):
    # Componentes do dashboard
    header = fh.Header("Dashboard")
    chart_div = create_chart_component()
    stats_div = create_stats_component()

    # Constrói a estrutura do dashboard
    dashboard_html = fh.Html(
        fh.Body(
            header,
            fh.Section(
                fh.Div(chart_div, stats_div, class_name="dashboard-container")
            )
        )
    )

    return render(request, "dashboard.html", {"dashboard_html": str(dashboard_html)})
