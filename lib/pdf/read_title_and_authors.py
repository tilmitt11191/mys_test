
# -*- coding: utf-8 -*-

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/utils")
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lib/pdf")

from pdf import PDF as pdf
pdf = pdf()
pdf.read_title_authors_keywords(by="file", var="../../data/samples/twitch.pdf")

from pdf import PDF as pdf
pdf2 = pdf()
pdf2.read_title_authors_keywords(by="file", var="../../data/samples/Comprehensive Study of Buffering Mechanisms inHybrid Live P2P Streaming Protocol HLPSP.pdf")

