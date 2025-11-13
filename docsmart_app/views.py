from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import UploadForm
from .models import Document
from .services.extractor import extract_text_from_pdf
from .services.classifier_stub import predict_label
from .services.summarizer_stub import summarize_text




def home_view(request):
    return redirect('upload')

def upload_view(request):
    result = None
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            file_obj = request.FILES.get('file')
            text = extract_text_from_pdf(file_obj)
            doc.extracted_text = text
            label, conf = predict_label(text)
            doc.label = label
            doc.confidence = conf
            doc.summary = summarize_text(text)
            doc.save()
            return redirect('result', pk=doc.pk)
    else:
        form = UploadForm()
        return render(request, 'docsmart_app/upload.html', {'form': form})


def result_view(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    return render(request, 'docsmart_app/result.html', {'doc': doc})


def list_view(request):
    try:
        docs = Document.objects.order_by('-created_at')[:50]
    except Exception as e:
        # log qılsa jaqsı boladı, bıraq userge akwayı xabar qaytaramız
        docs = []
    return render(request, 'docsmart_app/list.html', {'docs': docs})


