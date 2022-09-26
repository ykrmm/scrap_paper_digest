# Scrap Paper Digest Highlights conf 

## Step 1: Go to [Conference Paper Digests by Year](https://www.paperdigest.org/conference-paper-digest/)

Select the url of the conference you want scrap.

Example ICML 2022 Conference : https://www.paperdigest.org/2022/07/icml-2022-highlights/


## Step 2 : Run the program scrapper with your key words

Search the key words 'graph' AND 'dynamic' only in the title

`python scrap_paper_digest.py --url https://www.paperdigest.org/2022/07/icml-2022-highlights/ -w graph dynamic --all > dynamic.txt`

Search the key words 'graph' OR 'dynamic' only in the title

`python scrap_paper_digest.py --url https://www.paperdigest.org/2022/07/icml-2022-highlights/ -w graph dynamic > dynamic.txt`

Search the key words 'graph' OR 'dynamic' in the title AND in  the highlights 

`python scrap_paper_digest.py --url https://www.paperdigest.org/2022/07/icml-2022-highlights/ -w graph dynamic --search_highlights > dynamic.txt`


## Results example: 

`python scrap_paper_digest.py --url https://www.paperdigest.org/2022/04/www-2022-highlights/ -w graph dynamic --all --search_highlights`



```
- A New Dynamic Algorithm for Densest Subhypergraphs


Highlight: This algorithm worked only on unweighted hypergraphs, and had an approximation ratio of (1 +?)r2 and an update time of O(poly(r, log?n)), where r denotes the maximum rank of the input across all the updates. We obtain a new algorithm for this problem, which works even when the input hypergraph is weighted.


- TREND: TempoRal Event and Node Dynamics for Graph Representation Learning


Highlight: In this work, We propose TREND, a novel framework for temporal graph representation learning, driven by TempoRal Event and Node Dynamics and built upon a Hawkes process-based graph neural network (GNN).


- Multimodal Continual Graph Learning with Neural Architecture Search


Highlight: However, considering multimodal continual graph learning with evolving topological structures poses great challenges: i) it is unclear how to incorporate the multimodal information into continual graph learning and ii) it is nontrivial to design models that can capture the structure-evolving dynamics in continual graph learning. To tackle these challenges, in this paper we propose a novel Multimodal Structure-evolving Continual Graph Learning (MSCGL) model, which continually learns both the model architecture and the corresponding parameters for Adaptive Multimodal Graph Neural Network (AdaMGNN).


3 Papers found matching your search

```

