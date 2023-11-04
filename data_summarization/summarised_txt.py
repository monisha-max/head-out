import google.generativeai as palm

from data_summarization.processing import auto_select_coloumn, create_input_str, llm

palm.configure(api_key="AIzaSyBATda5w9AEGCb0PPvMQ02n1xo7-uAWtV0")


def get_summarised_txt(df, columns: list = [], autodetect: bool = True) -> list:
    """
    Function to return summarized text

    Params
    ------
    df: Pandas DataFrame
        Contains data from input csv file

    columns: list
        (Default is an empty list: case where user asks the LLM to choose columns)
        List whose elements are lists. Each of the elements contain columns that will be comapred to each other in the data analysis.

    autodetect: bool
        (Default is True: case where user expects LLM to autodetect which columns should be compared)
        If True: LLM autodetects
        If False: User inputs the columns that require a comparision"""
    # since we cant really take the inputs ourselves over here, we're gonna write the functions assuming that these inputs will be taken by monisha,
    # and some function she writes will pass these args to this function

    # TODO: will have to discuss if we need 2 ensure that 2<=len(col)<=4, or if monisha will do that

    if autodetect:
        columns = auto_select_coloumn(df.columns.to_list())
        print(columns)
        print(type(columns))
    outputs = list()
    for i in columns:
        ip = create_input_str(i, df)
        op = llm(ip)
        print(op)
        print("meow")
        outputs.append(op)

    return outputs
