# Sangkak-Challenge-IA

| Others languages    | Status      |
|-----------------|-------------|
| -> [Français](../README.md) | OK |
| -> ... | ... |
---------------------------------------------------------------------

**SANGKAK-CHALLENGE-IA** is an inter-datascientist and Natural Language Processing (NLP) researcher/engineer challenge aimed at creating concrete artificial intelligence solutions on an open-source dataset in African languages.

SANGKAK can be translated "To calculate while playing" in Yémba (language spoken in the department of Menoua in the West of Cameroon).

# Why create this challenge?


Africa has an unprecedented cultural and linguistic heritage. Its 3000 languages are still among the most under-resourced languages in the world, despite all the initiatives created in recent years on the continent. The challenges are very great and we have a major advantage today to radically change things: the technologies and applications of data science.

Working groups have sprung up on the continent in recent years and they have produced significant amounts of structured and unstructured resources for African languages. In addition to the lexicographic resources of the NTeALan Social Network association, we can also cite those of INALCO, the Masahkane collective, Google Research, Meta and many other organizations and universities around the world.

Some resources exist and even though a good part of these resources are private, they should now be exploited to create value within the linguistic companies concerned. All of this also involves identifying local issues, finding a possible link between these issues and available resources. This is one of the main reasons for this challenge project.

# February 2023 edition: organizational information

|                      |                                                                                                | Status           |
|----------------------|------------------------------------------------------------------------------------------------|------------------|
| Official website    | https://sangkak-challenge-ia.ntealan.net                                                       | In progress |
| Slack Community    | https://sangkak-challenge-ia.slack.com                                                      | OK |
| Edition              | February 2022                                                                                           | OK               |
| Topic          | Name Entities Recognition (NER)                                                                | OK               |
| Source data | MasakhaNER 2.0                                                                              | OK               |
| African languages    | bbj, bam, ewe, fon, hau, ibo, kin, lug, mos, nya, pcm , sna, swa, tsn, twi, wol, xho, yor, zul | OK               |


# How to participate in this February 2023 session?

## Context

The Masahkane organization, as part of a joint Lacuna Fund 2022 project, created and evaluated NER-annotated corpora, called **African NER Datasets**, in 20 sub-Saharan African languages. NER corpora produced in the CoNLL-03 format are currently shared in open access on their [official Github repository](https://github.com/masakhane-io/masakhane-ner/tree/main/MasakhaNER2.0/data)  or in the *data_source* folder of this [Github repository](https://github.com/NTeALan/Sangkak-Challenge-IA/data_source/masakhane-ner/MasakhaNER2.0/data).

The produced corpora were evaluated on NER tasks focusing on transfer learning technologies (Transformer) such as AfriBERTA, AfroXLMR, XLM-R, mBERT, etc. The results obtained were detailed in an article accepted at the conference [EMNLP 2022](https://2022.emnlp.org/) and accessible at this address  https://arxiv.org/abs/2210.12391.  On reading this document, we find that Ghomala, a language spoken in western Cameroon, has less interesting results in terms of performance compared to the other languages evaluated.

## Goals

The goal of this session is to challenge participants on the production of more efficient AI algorithms to detect named entities in the Ghomala language based on the work carried out by the Masahkane organization. These questions can guide you in choosing your theme:

- Which AI algorithm would be more appropriate to detect named entities in Ghomala and by extension to Bantu languages?
- How to better organize the data for this type of NLP task?
- Can Ghomala be treated like all other languages? Should we speak of a Ghomala specificity in NLP?
- What application can we put in place to help linguists or Ghomalaphone speakers to better deal with this problem?
- What methodology would be best suited to treat this type of stain?
- Would a combination of deterministic / probabilistic approach be a plus?

In any case, it is up to the participants to define their objectives and approaches to propose an effective NER detection solution on these data.

## Participate in the February 2023 session

To participate in this session and challenge other participants:

- Each participant or group of participants will have to appropriate the corpus [**African NER Datasets**](https://github.com/NTeALan/Sangkak-Challenge-IA/data_source/masakhane-ner/MasakhaNER2.0/data) by cloning this git directory.

- You then had to create a directory in your own Github space following this structure:

    - /data_source (being the reference to the NER Masahkane/optional corpora)
    - /evaluation
    - /training
    - methodology.md
    - license.md

- You must then propose your solution by respecting this structure. You are free to add other additional folders or files of your choice.

- Rename your folder with the initials of your project (Example: **ENR**) and then create a branch with the same initials, followed by a version number (Example: **ENR-0.1**)  and push it to your personal Github repository. (We will use this link as a git submodule of the **propossals** folder in this official challenge directory)

- Go back to this directory and enter your proposal in the file [PARTICIPANTS](./proposals/README.md) according to the fields provided. Then make a pull request so that the organizing committee validates your proposal and links your directory to this official directory.

Thank you for scrupulously respecting this procedure so that the organizing committee can better integrate your work into the official repertoire.

## Organizing committee

This challenge is organized by NTeALan Research and Development in collaboration with NTeALan Cameroon and NTeALan France.

- Elvis MBONING (Lead Data scientist NLP/NLU/Chatbot)
- Jean-Marc Bassahak (Lead Motion Design and web developer)
- Jules Assoumou (Vice rector of University of Ngaoundéré)
- ...


For any additional questions, do not hesitate to contact the challenge's organizing committee by [mail](sangkak-challenge-ia@ntealan.org) or the [Slack platform](https://join.slack.com/t/sangkak-challenge-ia/shared_invite/zt-1kxxxu4af-lQk~Kn6hmVI_OVNk6lqk~w).


## Sponsors

This challenge is sponsored by...

- ...
- ...
