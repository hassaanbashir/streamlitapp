# Define a function which takes 2 numberic list as an input
# and find the common element in the list

convs_list = open('E:\Hassaan Bashir\Projects\Streamlit\streamlitapp\cornell_movie_dialogs_corpus\cornell movie-dialogs corpus\movie_conversations.txt').read().split('\n')


conv_line_list = []
_conv_list = ""
for conv_list in convs_list:
    _conv_list = conv_list.split(' +++$+++ ')[-1].replace("'", "").replace(" ","").replace("[","").replace("]","")
    conv_line_list.append(_conv_list.split(','))
       

conv_line_list[1:3]