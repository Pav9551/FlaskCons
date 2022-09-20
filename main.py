from flask import render_template, Flask
import matplotlib.pyplot as plt
import io
import base64


app = Flask(__name__)


@app.get('/index')
@app.get('/')
def index():
    # img = io.BytesIO()
    #
    # y = [1, 2, 3, 4, 5]
    # x = [0, 2, 1, 3, 4]
    # plt.plot(x, y)
    # plt.savefig(img, format='png')
    # img.seek(0)
    #
    # plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('index.html')
# sio1 = io.BytesIO()
# fig1.savefig(sio1, format='png')
# dat = base64.b64encode(sio1.getvalue()).decode()


@app.get('/plot')
def new_ind():
    return render_template('n1.html')
