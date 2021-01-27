CLASSES
    tkinter.Tk(tkinter.Misc, tkinter.Wm)
        Mainframe

    class Mainframe(tkinter.Tk)
     |  Een 'MainFrame' object dat geinstantieerd wordt met tk.TK.
     |  Dit dient als venster van het programma en vanuit dit venster
     |  kan er genavigeerd worden
     |
     |  Method resolution order:
     |      Mainframe
     |      tkinter.Tk
     |      tkinter.Misc
     |      tkinter.Wm
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self)
     |      Return a new Toplevel widget on screen SCREENNAME. A new Tcl interpreter will
     |      be created. BASENAME will be used for the identification of the profile file (see
     |      readprofile).
     |      It is constructed from sys.argv[0] without extensions if None is given. CLASSNAME
     |      is the name of the widget class.
     |
     |  change(self, frame)
     |      Verandert frame o.b.v. ingevoerde frame
     |
     |  start(self)
     |      Keert terug naar startscherm als er op start gedrukt wordt
     |
     |  ----------------------------------------------------------------------

NAME
    voorspelframe

CLASSES
    builtins.object
        Voorspel

    class Voorspel(builtins.object)
     |  Voorspel(root)
     |
     |  Methods defined here:
     |
     |  __init__(self, root)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  show_answer(self, values)
     |      Geeft de uitkomst van de voorspellingen nadat de gebruiker de velden heeft ingevuld
     |
     |  voorspel_venster(self)
     |      Toont een venster waar de gebruiker voorspellingen kan doen
     |
     |  ----------------------------------------------------------------------

CLASSES
    builtins.object
        ErrorRegression

    class ErrorRegression(builtins.object)
     |  ErrorRegression(actual, predicted)
     |
     |  Methods defined here:
     |
     |  __init__(self, actual, predicted)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  calculate_residuals(self)
     |      Berekent residuals o.b.v. actual en predicted
     |
     |  rmseBerekenen(self)
     |      Geeft rmse terug
     |
     |  rootsquaredBerekenen(self)
     |      Geeft r2 terug
     |
     |  show_boxplot(self)
     |      Laat een weergave van een Boxplot van de residuals met de bijbehorende
     |      mean, median, min value en max value

NAME
    classificationerror

CLASSES
    builtins.object
        ErrorClassification

    class ErrorClassification(builtins.object)
     |  ErrorClassification(actual, predicted)
     |
     |  Methods defined here:
     |
     |  __init__(self, actual, predicted)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  showConfusionMatrix(self)
     |      Laat een confussion matrix zien van de actual en predicted
     |      en de daarbij behorende presision en recall
     |
     |  show_accuracy(self)
     |      Geeft de accuracy terug
     |
     |  show_precision(self)
     |      Geeft de precision score terug
     |
     |  show_recall(self)
     |      Geeft de recall score terug


NAME
    modelhandler

CLASSES
    builtins.object
        Model

    class Model(builtins.object)
     |  Model(id, naam, train_percentage, df, X, y, scaling, soort)
     |
     |  Class model
     |
     |  Methods defined here:
     |
     |  __init__(self, id, naam, train_percentage, df, X, y, scaling, soort)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  maak_model(self, k=5)
     |      Maakt een model aan op basis van meegegeven techniek
     |
     |  show_extensive_summary(self)
     |      Laat een uitgebreide summary zien van de errors o.b.v. classification of regression
     |
     |  show_summary_label(self)
     |      Laat het de naam, accuracy, r2 en type scaling zien op basis van type voorspelling
     |
     |  split_data(self)
     |      Split de trainingsdata o.b.v. type scaling en trainingspercentage
     |
     |  voorspel_uitkomst(self, waardes)
     |      Predict een uitkomst op basis van ingevoerde waardes
     
NAME
    bestmodelgenerator

CLASSES
    builtins.object
        Bestmodel

    class Bestmodel(builtins.object)
     |  Bestmodel(root, k)
     |
     |  Methods defined here:
     |
     |  __init__(self, root, k)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  best_model_frame(self)
     |      Summary venster zien
     |
     |  extensive_summary_model(self, tree)
     |      Laat een uitgebreide error summary zien als de gebruiker op de knop drukt
     |
     |  generate_best_knn_classification(self)
     |      Geneert het beste model o.b.v. de K threshold.
     |
     |  generate_best_knn_regression(self)
     |      Geneert het beste model o.b.v. de K threshold.
     |
     |  generate_decisiontreeClassification(self)
     |      Selecteer het beste decision tree regression model op
     |      basis van de 'max leaves nodes' en accuracy score
     |
     |  generate_decisiontreeRegression(self)
     |      Selecteer het beste decision tree regression model op
     |      basis van de 'max leaves nodes' en rmse score
     |
     |  generate_logistic_model(self)
     |      Genereert logistic regression model
     |
     |  generate_mlr_model(self)
     |      Genereert MLR model
     |
     |  laad_model_classification(self)
     |      Laad een classification model in op basis van selectie
     |
     |  laad_model_regression(self)
     |      Laad een regression model in op basis van selectie
     |
     |  model_laden(self, tree, venster)
     |      Laad een model in
     |
     |  show_best_models_classification(self, window)
     |      Laat alle beste modellen binnen classification zien
     |
     |  show_best_models_regression(self, window)
     |      Laat alle beste modellen binnen classification zien

NAME
    RegressionFrame

CLASSES
    builtins.object
        Regression

    class Regression(builtins.object)
     |  Regression(tk.Frame)
     |
     |  Methods defined here:
     |
     |  __init__(self, root, k)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  train_button(self, box, dataframe)
     |      Verwijdert NaN values uit dataframe en maakt een object(Bestmodel) aan
     |      waarbij het beste model word gegenereerd op basis van de ingevoerde variabelen
     |
     |  show_colums(self, tree)
     |      Weergeeft de column
     |
     |  add_independent_var(self, columns)
     |      Voegt de geselecteerde variabel toe aan self.X
     |
     |  remove_independent_var(self)(self)
     |      Verwijdert geselecteerd variabel uit self.X
     |
     |  get_categorical_columns(self)
     |      Selecteert de categorische columns uit df
     |     
     |  choose_dependent_val(self,dependent)
     |      Stel de dependent variabel in
     |
     |  clear(self)
     |      Wis het het huidige model en zet alle parameters terug naar hun beginwaardes

NAME
    ClassificationFrame

CLASSES
    builtins.object
        Classification

    class Regression(builtins.object)
     |  Classification(tk.Frame)
     |
     |  Methods defined here:
     |
     |  __init__(self, root, k)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  train_button(self, box, dataframe)
     |      Verwijdert NaN values uit dataframe en maakt een object(Bestmodel) aan
     |      waarbij het beste model word gegenereerd op basis van de ingevoerde variabelen
     |
     |  show_colums(self, tree)
     |      Weergeeft de column
     |
     |  add_independent_var(self, columns)
     |      Voegt de geselecteerde variabel toe aan self.X
     |
     |  remove_independent_var(self)(self)
     |      Verwijdert geselecteerd variabel uit self.X
     |
     |  get_categorical_columns(self)
     |      Selecteert de categorische columns uit df
     |     
     |  choose_dependent_val(self,dependent)
     |      Stel de dependent variabel in
     |
     |  clear(self)
     |      Wis het het huidige model en zet alle parameters terug naar hun beginwaardes
     

NAME
    geavanceerdframe

CLASSES
    builtins.object
        Geavanceerd

    class Geavanceerd(builtins.object)
     |  Geavanceerd(root)
     |
     |  Methods defined here:
     |
     |  __init__(self, root)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  apply_cutoff(self, value)
     |      Past de cutoff value aan op basis van input gebruiker
     |
     |  apply_process_parameter(self, train, scaling)
     |      Past de train % en type scaling aan op basis van input gebruiker
     |
     |  apply_threshold_k(self, k)
     |      Past de K threshold aan o.b.v. input gebruiker
     |
     |  geavanceerd_venster(self)
     |      Toont het geavanceerde venster

