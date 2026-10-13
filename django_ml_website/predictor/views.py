from django.shortcuts import render
from django.views.decorators.http import require_http_methods

def home(request):
    return render(request, "predictor/home.html")

@require_http_methods(["GET", "POST"])
def predict(request):
    context = {"prediction": None, "error": None, "area": "", "bedrooms": "", "location_factor": "1.0"}
    if request.method == "POST":
        context["area"] = request.POST.get("area", "").strip()
        context["bedrooms"] = request.POST.get("bedrooms", "").strip()
        context["location_factor"] = request.POST.get("location_factor", "1.0").strip()
        try:
            area = float(context["area"]); bedrooms = int(context["bedrooms"]); factor = float(context["location_factor"])
            if area <= 0 or bedrooms < 1 or factor <= 0: raise ValueError
            # DEMO ONLY: illustrative formula, not a trained ML model.
            estimated_price = (area * 4500 + bedrooms * 250000) * factor
            context["prediction"] = f"₹{estimated_price:,.0f}"
        except (ValueError, TypeError):
            context["error"] = "Enter a positive area, at least 1 bedroom, and a valid location factor."
    return render(request, "predictor/predict.html", context)
