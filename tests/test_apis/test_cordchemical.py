import unittest
from biothings_explorer.registry import Registry
from biothings_explorer.user_query_dispatcher import SingleEdgeQueryDispatcher
from .utils import get_apis

reg = Registry()

class TestSingleHopQuery(unittest.TestCase):

    def test_chemical2protein(self):
        """Test gene-protein"""
        seqd = SingleEdgeQueryDispatcher(output_cls='Protein',
                                         input_cls='ChemicalSubstance',
                                         input_id='CHEBI',
                                         pred="related_to",
                                         values='CHEBI:28640')
        seqd.query()
        self.assertTrue('PR:000000103' in seqd.G)
        self.assertTrue('PR:000000134' in seqd.G)
        edges = seqd.G['CHEBI:CHEBI:28640']['PR:000000134']
        self.assertTrue('CORD Chemical API' in get_apis(edges))

    def test_chemical2genomicentity(self):
        """Test gene-protein"""
        seqd = SingleEdgeQueryDispatcher(output_cls='GenomicEntity',
                                         input_cls='ChemicalSubstance',
                                         pred="related_to",
                                         input_id='CHEBI',
                                         values='CHEBI:28640')
        seqd.query()
        self.assertTrue('SO:0000165' in seqd.G)
        self.assertTrue('SO:0000331' in seqd.G)

    def test_chemical2chemicalsubstance(self):
        """Test gene-genomic entity"""
        seqd = SingleEdgeQueryDispatcher(output_cls='ChemicalSubstance',
                                         input_cls='ChemicalSubstance',
                                         input_id='CHEBI',
                                         values='CHEBI:28640')
        seqd.query()
        self.assertTrue('NITRIC OXIDE' in seqd.G)
        self.assertTrue('IMIQUIMOD' in seqd.G)
        edges = seqd.G['CHEBI:CHEBI:28640']['IMIQUIMOD']
        self.assertTrue('CORD Chemical API' in get_apis(edges))

    def test_chemical2gene(self):
        """Test gene-gene"""
        seqd = SingleEdgeQueryDispatcher(output_cls='Gene',
                                         input_cls='ChemicalSubstance',
                                         input_id='CHEBI',
                                         values='CHEBI:28640')
        seqd.query()
        self.assertTrue('SPG21' in seqd.G)
        self.assertTrue('LTA' in seqd.G)
        edges = seqd.G['CHEBI:CHEBI:28640']['SPG21']
        self.assertTrue('CORD Chemical API' in get_apis(edges))

    def test_chemical2anatomy(self):
        """Test gene-anatomy"""
        seqd = SingleEdgeQueryDispatcher(output_cls='AnatomicalEntity',
                                         input_cls='ChemicalSubstance',
                                         input_id='CHEBI',
                                         values='CHEBI:28640')
        seqd.query()
        self.assertTrue("UBERON:0000014" in seqd.G)
        edges = seqd.G['CHEBI:CHEBI:28640']['UBERON:0000014']
        self.assertTrue('CORD Chemical API' in get_apis(edges))

    def test_chemical2ma(self):
        """Test gene-molecular_activity"""
        seqd = SingleEdgeQueryDispatcher(output_cls='MolecularActivity',
                                         input_cls='ChemicalSubstance',
                                         input_id='CHEBI',
                                         values='CHEBI:28640')
        seqd.query()
        self.assertTrue("MOP:0000568" in seqd.G)
        self.assertTrue("CYTOKINE ACTIVITY" in seqd.G)
        edges = seqd.G['CHEBI:CHEBI:28640']['MOP:0000568']
        self.assertTrue('CORD Chemical API' in get_apis(edges))

    def test_chemical2bp(self):
        """Test gene-biological_process"""
        seqd = SingleEdgeQueryDispatcher(output_cls='BiologicalProcess',
                                         input_cls='ChemicalSubstance',
                                         input_id='CHEBI',
                                         values='CHEBI:28640')
        seqd.query()
        self.assertTrue('INFLAMMATORY RESPONSE' in seqd.G)
        self.assertTrue('PHAGOCYTOSIS' in seqd.G)
        edges = seqd.G['CHEBI:CHEBI:28640']['PHAGOCYTOSIS']
        self.assertTrue('CORD Chemical API' in get_apis(edges))

    def test_chemical2cc(self):
        """Test gene-cellular_component"""
        seqd = SingleEdgeQueryDispatcher(output_cls='CellularComponent',
                                         input_cls='ChemicalSubstance',
                                         input_id='CHEBI',
                                         values='CHEBI:28640')
        seqd.query()
        self.assertTrue('VIRION' in seqd.G)
        edges = seqd.G['CHEBI:CHEBI:28640']['VIRION']
        self.assertTrue('CORD Chemical API' in get_apis(edges))

    def test_chemical2cell(self):
        """Test gene-cell"""
        seqd = SingleEdgeQueryDispatcher(output_cls='Cell',
                                         input_cls='ChemicalSubstance',
                                         input_id='CHEBI',
                                         values='CHEBI:28640')
        seqd.query()
        self.assertTrue('CL:0000990' in seqd.G)

    def test_chemical2disease(self):
        """Test gene-disease"""
        seqd = SingleEdgeQueryDispatcher(output_cls='Disease',
                                         input_cls='ChemicalSubstance',
                                         input_id='CHEBI',
                                         values='CHEBI:28640')
        seqd.query()
        self.assertTrue('GASTROINTESTINAL MUCOSITIS' in seqd.G)
        edges = seqd.G['CHEBI:CHEBI:28640']['GASTROINTESTINAL MUCOSITIS']
        self.assertTrue('CORD Chemical API' in get_apis(edges))
