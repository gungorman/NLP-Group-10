'''Imports'''
import json


'''Pre-Processing'''
def load_reddit_comment_data(data_directory):

    comments_data = [] # list object that will store the loaded Reddit comments

    # we first open the file that includes our dataset
    with open(data_directory, 'r', encoding='utf-8') as f:
        # iterate the file, reading it line by line
        for line in f:
            # load the data petraining to a line into a json object in memory
            data = json.loads(line)

            # append the comment
            comments_data.append(data['body'])

    # the method returns all the loaded Reddit comments
    return comments_data

data_dir_comments = r"C:\Users\gungo\OneDrive\Desktop\stocks_comments.ndjson"
data_dir_sub = r"C:\Users\gungo\OneDrive\Desktop\stocks_submissions.ndjson"
reddit_data = load_reddit_comment_data(data_dir_)
print("Successfully loaded Reddit comments! Our dataset includes %d Reddit comments!" %len(reddit_data))
print(data_dir)