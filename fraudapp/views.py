from django.shortcuts import render
import pandas as pd
from io import TextIOWrapper
from django.template.defaulttags import register


# ✅ Jinja helper to fetch cell value by column name
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


# ✅ Fraud rules
def detect(df):
    df['is_fraud'] = False

    # high amount rule
    df.loc[df['amount'] > 100000, 'is_fraud'] = True

    # high-risk category
    df.loc[df['category'].str.lower().isin(['crypto', 'unknown']), 'is_fraud'] = True

    # suspicious country
    df.loc[df['country'].str.upper().isin(['US', 'GB', 'JP', 'CN']), 'is_fraud'] = True

    return df


# ✅ Home Page
def index(request):
    return render(request, "index.html")


# ✅ Upload → Detect → Send table data (NO DATABASE)
def upload_csv(request):
    if request.method == "POST":
        csv_file = request.FILES.get('csv_file')
        
        # Read file
        df = pd.read_csv(TextIOWrapper(csv_file.file, encoding='utf-8'))

        # Apply fraud detection rules
        df = detect(df)

        # Convert to Python dict for template loop
        context = {
            "table": {
                "columns": df.columns,
                "data": df.to_dict('records')
            }
        }
        return render(request, "result.html", context)

    return render(request, "upload.html")
