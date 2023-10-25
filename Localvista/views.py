from django.shortcuts import render

def create_html_view(html_page_name):
    def html_view(request):
        # You can add any context data you want to pass to the HTML template here.
        context = {
            'example_data': 'Hello, this is an example data.'
        }

        # Render the specified HTML page with the given context.
        return render(request, html_page_name, context)

    return html_view