import spacy
import streamlit as st
from streamlit import pyplot as plt #insted of matplotlib
import os
import networkx as nx



nlp = spacy.load("en_core_web_sm")

st.title("_PROJECT")

uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True) #used to browse

for uploaded_file in uploaded_files:
    # bytes_d = uploaded_file.read()
    bytes_data = uploaded_file.read() #reading the file
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

# print(filename)
    bytes_data = bytes_data.decode('utf-8')
    for x in bytes_data:
        print(f"Bytes data: {bytes_data}")
        # print(x.split(","))
    list_sent = bytes_data.split(",")
    st.write(list_sent)

    print(list_sent)

    triple_list = []
    for i in list_sent:
        doc = nlp(i)
    #     print(i)
        for token in doc:
            temp_list = []
    #         print(token.text, token.dep_)

            if 'subj' in token.dep_ or 'compound' in token.dep_:
                n1 = token.text
            if 'obj' in token.dep_:
                n2 = token.text
            if 'ROOT' in token.dep_:
                e = token.text
        temp_list.append(n1)
        temp_list.append(e)
        temp_list.append(n2)
        triple_list.append(temp_list)

    st.write('You selected `%s`' % triple_list)

    input_ng = triple_list
    label_edge = {}
    G = nx.DiGraph()
    for i in input_ng:
        G.add_node(i[0])
        G.add_node(i[2])
        G.add_edge(i[0], i[2])
        label_edge[(i[0], i[2])] = i[1]
    print(label_edge)
    pos = nx.spring_layout(G)
    # plt.figure()
    nx.draw(G, with_labels=True, node_size=1000, node_color='cyan', node_shape='o')
    nx.draw_networkx_edge_labels(G,pos ,edge_labels = label_edge, font_color='red')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    # st.area_chart(plt)
    # print(triple_list)


    user_ip = st.text_input("Find!", "type Here!")
    if st.button("submit"):
        inp = user_ip.title()
        st.write(inp)


        def get_relationship(word, lable_edge):
            related_terms_list = []

            for item_tuple, relationship in lable_edge.items():
                if word in item_tuple:
                    k = []
                    k.extend(item_tuple)
                    #             k.remove(word)
                    k.append(relationship)

                    related_terms_list.append(k)

            return related_terms_list


        ip = get_relationship(user_ip, label_edge)
        print(ip)

        input_ng = ip
        print(input_ng)
        label_edge = {}
        G = nx.DiGraph()
        for i in input_ng:
            G.add_node(i[0])
            G.add_node(i[1])
            G.add_edge(i[0], i[1])
            label_edge[(i[0], i[1])] = i[2]

        print(label_edge)
        pos = nx.spring_layout(G)
        nx.draw(G, with_labels=True, node_size=1000, node_color='cyan', node_shape='o')
        nx.draw_networkx_edge_labels(G,pos ,edge_labels = label_edge, font_color='red')
        st.pyplot()


























#
#
#
# print("-----------------------------------------------------------------------------------------------------------------------")
# import spacy
# import streamlit as st
# from streamlit import pyplot as plt
# import os
# import networkx as nx
#
#
#
# nlp = spacy.load("en_core_web_sm")
#
# st.title("_PROJECT")
#
# filename = st.text_input('Enter a file path:')
# try:
#     with open(filename) as input:
#         st.text(input.read())
# except FileNotFoundError:
#     print('File not found.')
#
# f = open(filename, "r")
# # print(f.read())
# for x in f:
#     print(x.split(","))
#     list_sent = x.split(",")
#
# st.write('You selected `%s`' % list_sent)
#
# triple_list = []
# for i in list_sent:
#     doc = nlp(i)
# #     print(i)
#     for token in doc:
#         temp_list = []
# #         print(token.text, token.dep_)
#
#         if 'subj' in token.dep_ or 'compound' in token.dep_:
#             n1 = token.text
#         if 'obj' in token.dep_:
#             n2 = token.text
#         if 'ROOT' in token.dep_:
#             e = token.text
#     temp_list.append(n1)
#     temp_list.append(e)
#     temp_list.append(n2)
#     triple_list.append(temp_list)
#
# st.write('You selected `%s`' % triple_list)
#
# input_ng = triple_list
# label_edge = {}
# G = nx.DiGraph()
# for i in input_ng:
#     G.add_node(i[0])
#     G.add_node(i[2])
#     G.add_edge(i[0], i[2])
#     label_edge[(i[0], i[2])] = i[1]
# print(label_edge)
# pos = nx.spring_layout(G)
# # plt.figure()
# nx.draw(G, with_labels=True, node_size=1000, node_color='cyan', node_shape='o') #with_labels to get the names
# nx.draw_networkx_edge_labels(G,pos ,edge_labels = label_edge, font_color='red')
# st.set_option('deprecation.showPyplotGlobalUse', False)
# st.pyplot()
# # st.area_chart(plt)
# # print(triple_list)
#
#
# user_ip = st.text_input("Find!", "type Here!")
# if st.button("submit"):
#     inp = user_ip.title()
# st.write(inp)
#
#
# def get_relationship(word, lable_edge):
#     related_terms_list = []
#
#     for item_tuple, relationship in lable_edge.items():
#         if word in item_tuple:
#             k = []
#             k.extend(item_tuple)
#             #             k.remove(word)
#             k.append(relationship)
#
#             related_terms_list.append(k)
#
#     return related_terms_list
#
#
# ip = get_relationship(user_ip, label_edge)
# print(ip)
#
# input_ng = ip
# print(input_ng)
# label_edge = {}
# G = nx.DiGraph()
# for i in input_ng:
#     G.add_node(i[0])
#     G.add_node(i[1])
#     G.add_edge(i[0], i[1])
#     label_edge[(i[0], i[1])] = i[2]
#
# print(label_edge)
# pos = nx.spring_layout(G)
# nx.draw(G, with_labels=True, node_size=1000, node_color='cyan', node_shape='o') #with_labels to get the names
# nx.draw_networkx_edge_labels(G,pos ,edge_labels = label_edge, font_color='red')
# st.pyplot()