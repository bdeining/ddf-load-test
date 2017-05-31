import xml.etree.cElementTree as ET
import os
import uuid
import random
from xml.dom.minidom import parse, parseString

def generate_xml_files(directory, num_files):
    for i in range(0, num_files):
        generate_xml(directory, str(i))


def generate_xml(directory, id):
    root = ET.Element("DOCUMENT")
    dict = generate_document_elements_map()

    for key, value in dict.items():
        ET.SubElement(root, key).text = value
    dir = os.path.dirname(__file__)
    temp = pretty_print(ET, root)
    f = open(dir + "/" + id + ".xml", 'w')
    f.write(temp)

def generate_document_elements_map():
    dict = {}
    dict["DRETITLE"] = get_random_sentence(3)
    dict["DREREFERENCE"] = "a reference"
    dict["UUID"] = str(uuid.uuid4())
    dict["AUTN_GROUP"] = "Connector"
    dict["AUTN_IDENTIFIER"] = "a"
    dict["AUTN_TASK_BATCH_ID"] = "a"
    dict["DocTrackingId"] = "a"
    dict["DESCRIPTION"] = get_random_sentence(10)
    dict["DREDATE"] = "a"
    dict["DATE_CREATED"] = "a"
    dict["DREDBNAME"] = "GeoSQRL"
    dict["ImportVersion"] = "a"
    dict["CONTENT_TYPE_NAME"] = "a"
    dict["KeyviewVersion"] = "a"
    dict["IA_MISSION_TAXONOMY"] = "a"
    dict["KEYWORD"] = get_random_word()
    return dict

def pretty_print(ET, root):
    original = ET.tostring(root, 'utf-8')
    reparsed = parseString(original)
    return reparsed.toprettyxml(indent="\t")

def get_random_date():

    return ""

def get_random_sentence(num_words):
    result = ""
    for i in range(0, num_words):
        result += get_random_word() + " "
    return result.strip()

def get_random_word():
    return random.choice(open(os.path.dirname(__file__) + "/../wordsEn.txt").readlines()).strip()