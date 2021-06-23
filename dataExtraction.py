import pandas as pd


def dataframe(new_filepath):
    """ Create a dataframe of the LifeCycle.csv file """
    data = pd.read_csv(new_filepath)
    # Clearing white spaces from columns (else KeyError is raised)
    data.columns = data.columns.str.strip()
    main_data = data.iloc[:, : 4]
    return main_data
