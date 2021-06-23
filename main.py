import reqData as rD
import dataExtraction as dE


def main():
    # File name of the original file
    # CSV file to be pasted in the same folder as the main file
    original_filename = 'Life cycle.csv'
    new_filename = 'LifeCycle.csv'

    # Creating a new file with required data from original file
    new_filepath = rD.new_file(original_filename, new_filename)
    df = dE.dataframe(new_filepath)
    print(df)


if __name__ == '__main__':
    main()
