from flask import Flask, render_template, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/data")
def get_data():
    return jsonify({"message": "Hello, Flask!"})

@app.route("/insights")
def insights():
    # Load the dataset
    data = pd.read_csv('Public Healthcare Dataset_ Hospital - train_data.csv.csv')

    # Generate insights
    # Example: Distribution of 'Severity of Illness'
    plt.figure(figsize=(10, 6))
    # sns.countplot(data['Severity of Illness'])
    sns.countplot(x='Severity of Illness', data=data)
    plt.title('Distribution of Severity of Illness')
    plt.xlabel('Severity of Illness')
    plt.ylabel('Count')

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template("insights.html", plot_url=plot_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
