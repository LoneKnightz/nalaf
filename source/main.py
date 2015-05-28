from utils.readers import HTMLReader
from preprocessing.spliters import NLTKSplitter
from preprocessing.tokenizers import NLTKTokenizer
from preprocessing.annotators import ReadFromAnnJsonAnnotator
from preprocessing.labelers import SimpleLabeler
from preprocessing.definers import TestNLDefiner
from features.simple import SimpleFeatureGenerator
from utils.crfsuite import CRFSuite

if __name__ == "__main__":

    html_path = r'C:\Users\Aleksandar\Desktop\Json and Html\IDP4_plain_html\pool'
    ann_path = r'C:\Users\Aleksandar\Desktop\Json and Html\IDP4_members_json\pool\abojchevski'
    crf_path = r'F:\Projects\crfsuite'

    dataset = HTMLReader(html_path).read()

    NLTKSplitter().split(dataset)
    NLTKTokenizer().tokenize(dataset)

    ReadFromAnnJsonAnnotator(ann_path).annotate(dataset)
    TestNLDefiner().define(dataset)
    print([ann.text for ann in dataset.annotations() if ann.is_nl]) #print the NL ones

    SimpleLabeler().label(dataset)
    SimpleFeatureGenerator().generate(dataset)

    crf = CRFSuite(crf_path)
    crf.create_input_file(dataset, 'train')
    crf.train()
    crf.create_input_file(dataset, 'test')
    crf.test()


