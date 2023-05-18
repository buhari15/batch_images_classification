from code.classify import app


if __name__ == "__main__":
    print("Loading the model please wait....")

    app.load_model_trained()
    app.run(debug=True)

 