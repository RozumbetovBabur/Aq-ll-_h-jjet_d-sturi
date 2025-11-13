# This is a *stub* classifier. Replace with a trained model for production.
# It returns a dummy label and confidence. Quick to run in environments
# where transformers/torch are not installed.


LABELS = ['ariza', 'esabat', 'budget', 'tech']

def predict_label(text):
    text = (text or '')[:1000].lower()
    if 'budget' in text or 'byudjet' in text:
        return 'budget', 0.9
    if 'kaz' in text or 'hisob' in text:
        return 'esabat', 0.8
    if len(text) < 200:
        return 'ariza', 0.6
    return 'tech', 0.5