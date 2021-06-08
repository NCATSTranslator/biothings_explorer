import unittest
from biothings_explorer.user_query_dispatcher import SingleEdgeQueryDispatcher
from .utils import get_apis


class TestSingleHopQuery(unittest.TestCase):
    def test_gene2chemical(self):
        """Test /gene/chemical_substance/{geneid} endpoint"""
        seqd = SingleEdgeQueryDispatcher(
            output_cls="ChemicalSubstance",
            input_cls="Gene",
            pred="related_to",
            input_id="NCBIGene",
            output_id="CHEBI",
            values="7852",
        )
        seqd.query()
        self.assertTrue("CHEBI:119486" in seqd.G)
        edges = seqd.G["NCBIGene:7852"]["CHEBI:119486"]
        self.assertTrue("Automat CORD19 Scibite API" in get_apis(edges))

    def test_chemical2disease(self):
        """Test /chemical_substance/disease/{chemicalid} endpoint"""
        seqd = SingleEdgeQueryDispatcher(
            input_cls="ChemicalSubstance",
            input_id="CHEBI",
            pred="related_to",
            output_cls="Disease",
            output_id="MONDO",
            values="CHEBI:6601",
        )
        seqd.query()
        self.assertTrue("MONDO:0005233" in seqd.G)
        self.assertTrue("MONDO:0011996" in seqd.G)
        edges = seqd.G["CHEBI:CHEBI:6601"]["MONDO:0005233"]
        self.assertTrue("Automat CORD19 Scibite API" in get_apis(edges))

    def test_chemical2gene(self):
        """Test /chemical_substance/gene/{chemicalid} endpoint"""
        seqd = SingleEdgeQueryDispatcher(
            input_cls="ChemicalSubstance",
            input_id="CHEBI",
            pred="related_to",
            output_cls="Gene",
            values="CHEBI:6601",
        )
        seqd.query()
        self.assertTrue("HMGB1" in seqd.G)
        self.assertTrue("TP53" in seqd.G)
        self.assertTrue("TNF" in seqd.G)
        edges = seqd.G["CHEBI:CHEBI:6601"]["HMGB1"]
        self.assertTrue("Automat CORD19 Scibite API" in get_apis(edges))

    def test_gene2disease(self):
        """Test /gene/disease/{geneid} endpoint"""
        seqd = SingleEdgeQueryDispatcher(
            input_cls="Gene",
            input_id="NCBIGene",
            pred="related_to",
            output_cls="Disease",
            values="7852",
        )
        seqd.query()
        self.assertTrue("epidermodysplasia verruciformis".upper() in seqd.G)
        edges = seqd.G["NCBIGene:7852"]["epidermodysplasia verruciformis".upper()]
        self.assertTrue("Automat CORD19 Scibite API" in get_apis(edges))

    def test_disease2gene(self):
        """Test /disease/gene/{diseaseid} endpoint"""
        seqd = SingleEdgeQueryDispatcher(
            input_cls="Disease",
            input_id="MONDO",
            pred="related_to",
            output_cls="Gene",
            values="MONDO:0007926",
        )
        seqd.query()
        self.assertTrue("FBF1" in seqd.G)
        self.assertTrue("UACA" in seqd.G)
        self.assertTrue("CXCR4" in seqd.G)
        edges = seqd.G["MONDO:MONDO:0007926"]["UACA"]
        self.assertTrue("Automat CORD19 Scibite API" in get_apis(edges))

    def test_disease2chemical(self):
        """Test /disease/chemical_substance/{diseaseid} endpoint"""
        seqd = SingleEdgeQueryDispatcher(
            input_cls="Disease",
            input_id="MONDO",
            output_id="CHEBI",
            pred="related_to",
            output_cls="ChemicalSubstance",
            values="MONDO:0007926",
        )
        seqd.query()
        self.assertTrue("CHEBI:28830" in seqd.G)
        edges = seqd.G["MONDO:MONDO:0007926"]["CHEBI:28830"]
        self.assertTrue("Automat CORD19 Scibite API" in get_apis(edges))
