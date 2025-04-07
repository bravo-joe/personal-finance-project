# Beginning of "app.py"
import faicons as fa
import plotly.express as px
import pandas as pd

# Load data and compute static values
from shinywidgets import render_plotly, output_widget

from shiny import reactive, render
from shiny.express import input, ui

# Parent directory
parent_dir = '/some/directory/'
# Get the data
plt1_data = pd.read_csv(parent_dir + 'plot1_data.csv')
plt2_data = pd.read_csv(parent_dir + 'plot2_data.csv')
boxplot_data = plt2_data.groupby("category").filter(lambda x: len(x) > 5)
plt3_data = pd.read_csv(parent_dir + 'plot3_data.csv')
plt3_data["sum"] = plt3_data['sum'].round(2)
tbl1_data = pd.read_csv(parent_dir + 'table1_data.csv')

# Add page title and sidebar
ui.page_opts(title="Personal Expenses", fillable=True)

# Add main content
ICONS = {
    "db": fa.icon_svg("database"),
    "currency-dollar": fa.icon_svg("dollar-sign"),
}

with ui.layout_columns(fill=False):
    with ui.value_box(showcase=ICONS["currency-dollar"]):
        "Total Spent"

        @render.express
        def total_spent():
            total = plt1_data['amount'].sum()
            f"${total:.2f}"

    with ui.value_box(showcase=ICONS["db"]):
        "Total Transactions"

        @render.express
        def total_txn():
            row_count = len(plt2_data)
            row_count

# with ui.layout_columns(col_widths=[6, 6, 12]):
with ui.layout_columns(col_widths=[4,4,4,12]):
    with ui.card(full_screen=True):
        ui.card_header("Expenses Table")

        @render.data_frame
        def table():
            return render.DataGrid(tbl1_data)

    with ui.card(full_screen=True):
        ui.card_header("Total spent per category")

        @render_plotly
        def barplot1():
            return px.bar(
                plt1_data,
                x="category",
                y="amount",
                color_discrete_sequence=['#2ca02c']
            )

    # with ui.card(full_screen=True):
    #     ui.card_header("Transactions n > 5")

        @render_plotly
        def box_plot():
            
            plt = px.box(
                boxplot_data,
                x="category",
                y="amount",
                color_discrete_sequence=['#2F4F4F']
            )

            return plt
        
    with ui.card(full_screen=True):
        ui.card_header("Amount spent per day")

        @render_plotly
        def time_series():
            fig = px.line(
               plt3_data,
               x = "date",
               y = "sum",
               color_discrete_sequence=['#8B008B']
            )
            return fig

# End of "app.py"
