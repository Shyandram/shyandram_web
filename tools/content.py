"""Single source of truth for the site's content.

Edit this file, then run `python3 tools/build.py` to regenerate the HTML.
Strings marked "html" may contain inline markup (<strong>, <em>, <a>).
"""

SITE_URL = "https://shyandram.dev/"
NAME = "Shyang-En Weng"
NAME_ZH = "翁祥恩"
SCHOLAR = "https://scholar.google.com/citations?user=DBBIjHsAAAAJ"
ORCID = "https://orcid.org/0000-0002-4663-7846"
ORCID_ID = "0000-0002-4663-7846"
GITHUB = "https://github.com/Shyandram"
LINKEDIN = "https://www.linkedin.com/in/Shyandram/"
MEDIUM = "https://medium.com/@shyangen104"
EMAIL = "shyangen104@gmail.com"
CV_URL = "https://drive.google.com/file/d/1rs0FKCtK_leqRvLHzdSkleJ6Lxe3RcTZ/view"
BLOG = "https://blog.shyandram.dev/zh-tw/"
SLIDES_URL = "https://drive.google.com/file/d/1j0LcNTCM60v78FmR7VG5Dv24tpJnl4ON/view"

# ----------------------------------------------------------------------------
# Home page
# ----------------------------------------------------------------------------
ABOUT = (
    "Currently a PhD candidate in Computer Science at NYCU, I hold dual Master's degrees in ECE from UWM "
    "and EL from CYCU. My research expertise lies in Image Processing, Pattern Recognition, and Deep Learning, "
    "with a focus on Image Restoration and Object Detection. I care about the gap between a promising model "
    "and a system that holds up in the real world."
)

FOCUS = [
    ("01", "Restore", "Recover detail, color, and visibility from degraded imagery."),
    ("02", "Recognize", "Turn visual signals into reliable, useful information."),
    ("03", "Deploy", "Keep models efficient enough for practical environments."),
]

EDUCATION = [
    {
        "date": "Feb 2025 - Present",
        "org": "National Yang Ming Chiao Tung University (NYCU)",
        "role": "Doctor of Philosophy in Computer Science and Engineering",
        "lines": ["ACM Lab (Applied Computing and Multimedia Lab). Focus on Computer Vision and Deep Learning."],
        "courses": [],
    },
    {
        "date": "Sep 2023 - May 2024",
        "org": "University of Wisconsin-Milwaukee (UWM)",
        "role": "Master of Science in Engineering (Dual Master's Degree Program)",
        "lines": ["Electrical and Computer Engineering Concentration"],
        "gpa": "3.833",
        "courses": [
            ("Signal Processing", "Digital Signal Processing, Communication Systems"),
            ("Machine Learning and Application",
             "Advanced Machine Learning, Natural Language Processing, Image Processing"),
        ],
    },
    {
        "date": "Sep 2022 - May 2024",
        "org": "Chung Yuan Christian University (CYCU)",
        "role": "Master of Science in Electronic Engineering (Dual Master's Degree Program)",
        "lines": ["Institute of Computer Science and Engineering"],
        "gpa": "4.000",
        "courses": [
            ("Pattern Recognition and Machine Learning",
             "Pattern Recognition, Optimization theory and applications, Advanced Digital Image Processing"),
            ("Application Design", "Android Application Design"),
        ],
    },
    {
        "date": "Sep 2017 - Jun 2022",
        "org": "Chung Yuan Christian University (CYCU)",
        "role": "Bachelor of Science in Electronic Engineering",
        "lines": ["Department of Electrical Engineering"],
        "gpa": "3.878 (161 total credits)",
        "extra": "Certificate of Cross-Disciplinary Program: Intelligent Robotics",
        "courses": [
            ("Computer Vision and Pattern Recognition",
             "Digital Image Processing, Pattern Recognition and Machine Learning"),
            ("Signals and Systems", "Information Theory, Communication System"),
            ("Semiconductor Manufacturing and IC Circuit Design",
             "Modern Physics, Semiconductor Physics, Semiconductor Technology Seminar; "
             "VLSI Testing, Computer-Aided Analog Circuit Design, Analysis, and Simulations"),
            ("Miscellaneous Subjects", "Robotics, Computer Networks, Programming and Algorithms"),
        ],
    },
]

EXPERIENCE = [
    {
        "date": "Feb 2025 - Present",
        "title": "Research Assistant (Part-time)",
        "org": "ACM Lab, National Yang Ming Chiao Tung University",
        "advisor": "Advisor: Prof. Ching-Chun Huang",
        "paras": [
            "Collaborating on a MediaTek industry-academic cooperation project, focusing on Super-Resolution, "
            "Diffusion Models, and Image Restoration.",
            "Assisted the proposal writing of NSTC Research Project and ITRI industry-academic cooperation project.",
        ],
        "bullets": [],
    },
    {
        "date": "Jan 2024 - Jul 2024",
        "title": "Research Assistant (Part-time)",
        "org": "MuCAT Lab, Chung Yuan Christian University (CYCU), Taiwan",
        "advisor": "Advisor: Prof. Shaou-Gang Miaou",
        "paras": [
            "Participated in a NSTC Research Project, focusing on Dynamic Illumination Adjustment and "
            "Super-Resolution.",
        ],
        "bullets": [
            "Guided an Engineering Design Project with undergraduate students.",
            "An undergraduate student was awarded the NSTC College Student Research Scholarship.",
            "Assisted the proposal writing of NSTC Research Project.",
            "Published works in Academic Journals and Conferences (SIVP, ICCE-TW, CVGIP).",
        ],
    },
    {
        "date": "Oct 2022 - Aug 2023",
        "title": "Research Assistant (Part-time)",
        "org": "MuCAT Lab, Chung Yuan Christian University (CYCU), Taiwan",
        "advisor": "Advisor: Prof. Shaou-Gang Miaou",
        "paras": [
            "Participated in a NSTC Research Project, focusing on Image Enhancement and Restoration, "
            "Lightweight AI for Edge Devices, and Industry Application of Computer Vision.",
        ],
        "bullets": [
            "Guided 3 Engineering Design Projects with undergraduate students.",
            "An undergraduate student was awarded the NSTC College Student Research Scholarship.",
            "Published works in Academic Journals and Conferences (IJPRAI, IS3C, CVGIP, ICASI)",
        ],
    },
    {
        "date": "Sep 2021 - Jan 2022",
        "title": "Teaching Assistant (Part-time)",
        "org": "Department of Electronic Engineering, Chung Yuan Christian University (CYCU), Taiwan",
        "advisor": "Instructor: Prof. Hui-Kai Zeng",
        "paras": ["Course: Modern Physics"],
        "bullets": [],
    },
    {
        "date": "Sep 2018 - Jun 2022",
        "title": "Student Senator",
        "org": "Department of Electronic Engineering Student Council, CYCU",
        "paras": ["Served as a Senator (議代) for the Department Student Council for 4 years."],
        "bullets": [],
    },
    {
        "date": "May 2019",
        "title": "Section Leader of Equipment Group",
        "org": "Activity of Host/Sponsor: Free Mother's Day Card",
        "paras": ["Certificate of the CYCU Holistic Education"],
        "bullets": [],
    },
]

AWARDS = [
    ("Jun 2023", "Best Conference Papers Award",
     "2023 IEEE International Symposium on Computer, Consumer and Control (IS3C2023)",
     "Paper: Reducing Computational Requirements of Image Dehazing Using Super-Resolution Networks"),
    ("Jun 2022", "CYCU Student Research Creativity Award",
     "Project: Mask Wearing Detection Based on Deep Learning Networks", ""),
    ("May 2022", "Certificate of Participation", "Taiwan AI EXPO AI Junior Award 2023",
     "Project: AI Home Assistant – Interactive Stereoscopic Visual Virtual Voice Assistant"),
    ("2021 - 2022", "Certificate of Excellence", "Department of Electronic Engineering, CYCU",
     "書卷獎, Awarded for semesters 109-2 and 110-1."),
    ("Dec 2021", "Silver Medal",
     "Third AI & Big Data Creative Competition, Chung Yuan Christian University",
     "Project: Deep Learning-Based System for Assessing Learning Effectiveness"),
    ("Jan 2021", "Certificate of Participation", "Full Custom IC Design Training Program",
     "Department of Electronic Engineering, Chung Yuan Christian University"),
]

# ----------------------------------------------------------------------------
# Publications. `project` links a paper to a project slug; `selected` puts it on the home page.
# type: journal | conference | preprint | thesis
# ----------------------------------------------------------------------------
PUBLICATIONS = [
    {
        "project": "diffusion-sr", "id": "osdiff-2026", "year": 2026, "type": "preprint", "selected": True,
        "title": "Bridging Restoration and Generation in One-step Diffusion for Real-World Image Super-Resolution",
        "authors": "Shyang-En Weng, Yi-Cheng Liao, Yu-Syuan Xu, Wei-Chen Chiu, Ching-Chun Huang",
        "venue": "arXiv preprint", "date": "Apr 2026",
        "links": [("arXiv:2604.24136", "https://arxiv.org/abs/2604.24136")],
    },
    {
        "id": "ntire-2026", "year": 2026, "type": "preprint", "selected": False,
        "title": "The First Challenge on Mobile Real-World Image Super-Resolution at NTIRE 2026: "
                 "Benchmark Results and Method Overview",
        "authors": "Jiatong Li and 93 other authors, including Shyang-En Weng",
        "venue": "arXiv preprint", "date": "Apr 2026",
        "links": [("arXiv:2604.17306", "https://arxiv.org/abs/2604.17306")],
    },
    {
        "project": "diffusion-sr", "id": "zephir-2025", "year": 2025, "type": "preprint", "selected": True,
        "title": "Learning Ordinal Degradation Representations with Textual Priors for Diffusion-Based "
                 "Blind Image Super-Resolution",
        "authors": "Yi-Cheng Liao, Shyang-En Weng, Yu-Syuan Xu, Chia-Hung Yuan, Wei-Chen Chiu, Ching-Chun Huang",
        "venue": "arXiv preprint", "date": "Dec 2025",
        "links": [("arXiv:2512.10340", "https://arxiv.org/abs/2512.10340")],
    },
    {
        "id": "ijprai-2025", "year": 2025, "type": "journal", "selected": True, "project": "lightweight-enhancement",
        "title": "A lightweight low-light image enhancement network via channel prior and gamma correction",
        "authors": "Shyang-En Weng, Shaou-Gang Miaou, Ricky Christanto",
        "venue": "International Journal of Pattern Recognition and Artificial Intelligence (IJPRAI), vol. 39, no. 12",
        "date": "2025",
        "links": [("DOI: 10.1142/S0218001425540138", "https://www.worldscientific.com/doi/full/10.1142/S0218001425540138"),
                  ("arXiv:2402.18147", "https://arxiv.org/abs/2402.18147")],
    },
    {
        "id": "jit-2025", "year": 2025, "type": "journal", "selected": True, "project": "mask-detection",
        "title": "An Integrated Approach to Mask Wearing Classification and Crowd Counting in Public Spaces "
                 "Using YOLOv5s and Deep SORT",
        "authors": "Shyang-En Weng, Ying-Cheng Lin, Ming-Yao Liang, Shaou-Gang Miaou",
        "venue": "Journal of Internet Technology, vol. 26, no. 4, pp. 423-434", "date": "Jul 2025",
        "links": [("JIT article", "https://jit.ndhu.edu.tw/article/view/3181"),
                  ("PDF", "https://drive.google.com/file/d/1aH6K4oJzWHm3O7tRLdsa136o_wgOWKWs/view?usp=sharing")],
    },
    {
        "id": "cpganet-plus-2024", "year": 2024, "type": "preprint", "selected": True,
        "project": "lightweight-enhancement",
        "title": "Rethinking Theoretical Illumination for Efficient Low-Light Image Enhancement",
        "authors": "Shyang-En Weng, Cheng-Yen Hsiao, Li-Wei Lu, Yu-Shen Huang, Tzu-Han Chen, Shaou-Gang Miaou, "
                   "Ricky Christanto",
        "venue": "arXiv preprint", "date": "Sep 2024",
        "links": [("arXiv:2409.05274", "https://arxiv.org/abs/2409.05274"),
                  ("Code", "https://github.com/Shyandram/CPGA-Net_Plus")],
    },
    {
        "id": "sivp-2024", "year": 2024, "type": "journal", "selected": True, "project": "dynamic-illuminance",
        "title": "Dynamic Illuminance Adjustment for Simultaneous Exposure Correction and Low-Light Image Enhancement",
        "authors": "Shyang-En Weng, Chang-Pin Hsu, Cheng-Yen Hsiao, Ricky Christanto, Shaou-Gang Miaou",
        "venue": "Signal, Image and Video Processing", "date": "Sep 2024",
        "links": [("DOI: 10.1007/s11760-024-03519-0", "https://doi.org/10.1007/s11760-024-03519-0")],
    },
    {
        "id": "cvgip-2024", "year": 2024, "type": "conference", "selected": False, "project": "dynamic-illuminance",
        "title": "Scene-Guided Image Enhancement through Gamma Correction Prior and Transfer Learning "
                 "for Varied Illumination Environments",
        "authors": "Shyang-En Weng, Cheng-Yen Hsiao, Chang-Pin Hsu, Shaou-Gang Miaou",
        "venue": "CVGIP 2024, Hualien, Taiwan", "date": "2024",
        "links": [("PDF", "https://drive.google.com/file/d/12UQGOyMK4EBdCErrsk_W5JYVBN7L8OD8/view?usp=sharing")],
    },
    {
        "id": "icce-2024", "year": 2024, "type": "conference", "selected": False, "project": "lightweight-enhancement",
        "title": "Exposure Correction in Driving Scenes Using the Atmospheric Scattering Model",
        "authors": "Shyang-En Weng, Shaou-Gang Miaou, Ricky Christanto, Chang-Pin Hsu",
        "venue": "IEEE ICCE-TW 2024, Taichung, Taiwan", "date": "2024",
        "links": [("DOI: 10.1109/ICCE-TW55602.2024.10674535", "https://ieeexplore.ieee.org/document/10674535/")],
    },
    {
        "id": "is3c-2023", "year": 2023, "type": "conference", "selected": False, "project": "dehazing-sr",
        "award": "Best Paper Award",
        "title": "Reducing Computational Requirements of Image Dehazing Using Super-Resolution Networks",
        "authors": "Shyang-En Weng, Yan-Gu Ye, Ying-Cheng Lin, Shaou-Gang Miaou",
        "venue": "IEEE IS3C 2023, Taichung, Taiwan", "date": "2023",
        "links": [("DOI: 10.1109/IS3C55602.2023.10219494", "https://ieeexplore.ieee.org/document/10219494")],
    },
    {
        "id": "icasi-2023", "year": 2023, "type": "conference", "selected": False, "project": "dehazing-sr",
        "title": "Using Stereo Depth Estimation Network and LiDAR-Assisted Camera for Dehazing",
        "authors": "Shih-Li Lu, Shaou-Gang Miaou, Shyang-En Weng, Ying-Cheng Lin",
        "venue": "2023 9th IEEE International Conference on Applied System Innovation (ICASI2023), Chiba, Japan",
        "date": "2023",
        "links": [("DOI: 10.1109/ICASI57738.2023.10179550", "https://ieeexplore.ieee.org/document/10179550")],
    },
    {
        "id": "cvgip-2023", "year": 2023, "type": "conference", "selected": False, "project": "hairstyle-recommendation",
        "title": "A Hair Style Recommendation System with Advanced FA, FS, and HDT",
        "authors": "Shyang-En Weng, Shaou-Gang Miaou",
        "venue": "CVGIP 2023, Taiwan", "date": "2023",
        "links": [("PDF", "https://drive.google.com/file/d/1m5GMriR5bY0f0rRyLAGze6_Gpg2QH2Yc/view?usp=sharing")],
    },
    {
        "id": "ssrn-2023", "year": 2023, "type": "preprint", "selected": False, "project": "weather-generation",
        "title": "A Non-Adversarial and End-to-End Deep Learning Generative Network for Generating Diverse "
                 "Weather Images",
        "authors": "Shyang-En Weng, Shaou-Gang Miaou",
        "venue": "SSRN preprint", "date": "Jan 2023",
        "links": [("SSRN: 4591716", "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4591716")],
    },
    {
        "id": "thesis-2024", "year": 2024, "type": "thesis", "selected": False, "project": "weather-generation",
        "title": "Weather Image Generation (DGNDW)",
        "authors": "Shyang-En Weng, Shaou-Gang Miaou",
        "venue": "Master's Thesis, CYCU", "date": "2024",
        "links": [("Thesis", "https://hdl.handle.net/11296/xjgq5j")],
    },
]

PUB_TYPES = {"journal": "Journal", "conference": "Conference", "preprint": "Preprint", "thesis": "Thesis"}

# ----------------------------------------------------------------------------
# Projects. `figures` are (path, alt) pairs; a project page places them where `fig:N` appears in a section.
# `fit` controls the card thumbnail: "contain" for diagrams, "cover" for photos.
# ----------------------------------------------------------------------------
PROJECTS = [
    {
        "slug": "diffusion-sr", "featured": True, "category": "restoration",
        "title": "Diffusion-based Real-World Super-Resolution",
        "title_zh": "基於擴散模型的真實世界超解析度",
        "year": "2025-2026", "short": "Diffusion SR",
        "summary": "Adapting pretrained diffusion models to real-world super-resolution with degradation-aware "
                   "representations and one-step restoration.",
        "chips": ["Diffusion Models", "Super-Resolution", "Degradation Representation", "arXiv 2025-2026"],
        "thumb": "images/Diffusion SR/cover.svg", "fit": "cover",
        "links": [("arXiv:2604.24136", "https://arxiv.org/abs/2604.24136"),
                  ("arXiv:2512.10340", "https://arxiv.org/abs/2512.10340")],
        "facts": [("Period", "2025-2026"),
                  ("Setting", "ACM Lab, NYCU, with MediaTek co-authors"),
                  ("Authorship", "1st author (2604.24136), 2nd author (2512.10340)")],
        "keywords": ["Real-World Super-Resolution", "Diffusion Models", "Stable Diffusion", "One-Step Diffusion",
                     "Degradation Representation", "CLIP"],
        "sections": [
            {"id": "overview", "title": "Project overview", "html": """
<p>Real-world image super-resolution (Real-ISR) has to restore images whose degradations are unknown, mixed and
of varying severity. This project studies how to make large pretrained diffusion models, such as
<strong>Stable Diffusion</strong>, work for that setting along two complementary directions: representing
<em>what</em> is wrong with an image and <em>how badly</em>, and using that knowledge to decide how a diffusion
model should restore it.</p>"""},
            {"id": "ordinal-degradation", "title": "Ordinal degradation representations", "html": """
<p>The first paper, <em>Learning Ordinal Degradation Representations with Textual Priors for Diffusion-Based
Blind Image Super-Resolution</em> (<a href="https://arxiv.org/abs/2512.10340" target="_blank" rel="noopener">arXiv:2512.10340</a>),
was first released as <strong>ZePHiR</strong>: zero-shot adaptation of Stable Diffusion through a plug-in
hierarchical degradation representation.</p>
<ul>
<li><strong>Decoupled degradation</strong>: an <strong>HD-CLIP</strong> component separates degradation
<em>type</em> from degradation <em>intensity</em> using composition-based ordinal text embeddings.</li>
<li><strong>Plug-in design</strong>: the representation is attached to a pretrained diffusion model rather than
training a restoration network from scratch.</li>
</ul>"""},
            {"id": "one-step", "title": "One-step diffusion with manifold inversion", "html": """
<p>The second paper, <em>Bridging Restoration and Generation in One-step Diffusion for Real-World Image
Super-Resolution</em> (<a href="https://arxiv.org/abs/2604.24136" target="_blank" rel="noopener">arXiv:2604.24136</a>),
targets the cost of iterative diffusion sampling. Distilling a diffusion model into a single step is fast but
runs into a perception-distortion trade-off: common one-step methods turn the generative prior into a
deterministic mapping and lose its stochastic nature, while methods that bring randomness back by shifting
timesteps or adding noise only control one side, so restoration and generation agree at a few preset timesteps
and drift apart once steered.</p>
<p>The proposed <strong>IDaS-SR</strong> (Inversion and Degradation-aware Sampling for Real-ISR) is a one-step
framework with two parts:</p>
<ul>
<li><strong>Manifold Inversion Noise Estimator</strong>: anchors the low-quality latent onto the pretrained
diffusion trajectory.</li>
<li><strong>CHARIOT</strong>: reintroduces controlled stochasticity, so a single scalar moves smoothly along the
fidelity-realism trade-off at inference.</li>
</ul>
<p>The authors report state-of-the-art results under explicit control in a single inference step.</p>"""},
        ],
    },
    {
        "slug": "dynamic-illuminance", "featured": True, "category": "enhancement",
        "title": "Dynamic Illuminance Enhancement for Diverse Scenes",
        "title_zh": "面對不同亮度場景的動態照明影像增強",
        "year": "2024", "short": "Dynamic Illuminance Adjustment",
        "summary": "Developing smart systems to handle extreme lighting variability in real-world environments.",
        "chips": ["Dynamic Illuminance Adjustment", "Exposure Correction", "NSTC-Research Project"],
        "card_chips": ["Illumination_Spectrum", "CPGADIA"],
        "thumb": "images/Dynamic Illuminance Enhancement/CPGADIA.webp", "fit": "contain",
        "links": [("GitHub Repository", "https://github.com/Shyandram/CPGA-DIA.git")],
        "facts": [("Context", "NSTC Research Project & University Student Grant"),
                  ("Period", "2024")],
        "keywords": ["Dynamic Illuminance Adjustment", "Low-Light Image Enhancement", "Exposure Correction",
                     "Multi-Task Learning", "Gamma Correction"],
        "sections": [
            {"id": "overview", "title": "Project overview", "figures": [
                ("images/Dynamic Illuminance Enhancement/Illumination_Spectrum.webp",
                 "Illumination Spectrum analysis")], "html": """
<p>This project addresses the challenge of <strong>Dynamic Illuminance Image Enhancement</strong> in diverse
lighting environments. From under-exposed night scenes to over-exposed daytime scenarios, the goal is to achieve
balanced visibility. This work is supported by the NSTC-Research Project "Lightweight Multi-Task Learning for
Dynamic Illuminance Enhancement in ADAS".</p>"""},
            {"id": "cpga-dia", "title": "Dynamic Illuminance Adjustment (CPGA-DIA)", "figures": [
                ("images/Dynamic Illuminance Enhancement/CPGADIA.webp", "Dynamic Illuminance Results")], "html": """
<p>Published in <em>Signal, Image and Video Processing</em>, this work proposes <strong>CPGA-DIA</strong>
(Channel Prior Gamma Adjustment for Dynamic Illuminance Adjustment), a multi-task framework designed for
<strong>Simultaneous Exposure Correction</strong>.</p>
<ul>
<li><strong>Unified Correction</strong>: A single framework capable of handling both low-light (under-exposed)
and over-exposed scenes simultaneously.</li>
<li><strong>Gamma Correction Prior</strong>: Introduces explicit gamma correction to effectively handle extreme
lighting variations while avoiding color artifacts.</li>
</ul>"""},
            {"id": "sgie", "title": "Scene-Guided Image Enhancement (SGIE)", "figures": [
                ("images/Dynamic Illuminance Enhancement/SGIE-CPGA.webp",
                 "Scene-Guided Image Enhancement Architecture")], "html": """
<p>Presented at <em>CVGIP 2024</em>, this research introduces a <strong>Scene-Guided</strong> strategy leveraging
<strong>Transfer Learning</strong> to adapt enhancement models to complex, varied illumination environments.</p>
<ul>
<li><strong>Transfer Learning</strong>: Utilizes pre-trained knowledge to adapt to specific lighting domains,
improving robustness.</li>
<li><strong>Scene-Guided Strategy</strong>: Classifies scene characteristics to dynamically adjust enhancement
parameters for optimal visibility.</li>
<li><strong>Gamma Correction Prior</strong>: Retains the core benefit of gamma prior for consistent structural
preservation.</li>
</ul>"""},
        ],
    },
    {
        "slug": "lightweight-enhancement", "featured": True, "category": "enhancement",
        "title": "Lightweight Deep Learning for Image Enhancement",
        "title_zh": "基於深度學習的輕量級影像增強方法",
        "year": "2024-2025", "short": "Lightweight enhancement",
        "summary": "Highly efficient neural networks designed for mobile devices and edge computing.",
        "chips": ["Edge AI", "Knowledge Distillation", "Explainable AI"],
        "card_chips": ["CPGA-Net", "CPGA-Net+"],
        "thumb": "images/Lightweight Image Enhancement/exposure.webp", "fit": "cover",
        "links": [("GitHub: CPGA-Net", "https://github.com/Shyandram/CPGA-Net-Pytorch.git"),
                  ("GitHub: CPGA-Net+", "https://github.com/Shyandram/CPGA-Net_Plus")],
        "facts": [("Period", "2024-2025"), ("Models", "CPGA-Net, CPGA-Net+"),
                  ("Footprint", "0.025 M parameters, 0.030 s inference (CPGA-Net)")],
        "keywords": ["Low-Light Enhancement", "Edge AI", "Knowledge Distillation", "Explainable AI",
                     "Model Compression", "Embedded Vision Systems"],
        "sections": [
            {"id": "overview", "title": "Project overview", "figures": [
                ("images/Lightweight Image Enhancement/exposure.webp", "Exposure Correction Results")], "html": """
<p>This research project focuses on developing <strong>Lightweight Low-Light Image Enhancement (LLIE)</strong>
algorithms capable of real-time processing on edge devices. The core innovation lies in the
<strong>CPGA-Net</strong> (Channel Prior and Gamma Estimation Network) and its advanced variant
<strong>CPGA-Net+</strong>, which utilize channel priors and adaptive gamma correction to robustly enhance
visibility in varying illumination conditions.</p>"""},
            {"id": "cpga-net", "title": "CPGA-Net: channel prior &amp; gamma correction", "figures": [
                ("images/Lightweight Image Enhancement/CPGAnet.webp", "CPGA-Net Architecture")], "html": """
<p>Introduced in our <em>IJPRAI</em> publication, <strong>CPGA-Net</strong> combines dark/bright channel priors
with deep learning-based gamma correction. Inspired by the Retinex theory and Atmospheric Scattering Model, this
architecture features:</p>
<ul>
<li><strong>Ultra-Lightweight Design</strong>: 0.025 million parameters with an inference time of 0.030s.</li>
<li><strong>Feature Distillation</strong>: Exploring knowledge transfer from complex teachers to compact student
models.</li>
<li><strong>Explainable Factors</strong>: Utilizing explicit gamma parameters for interpretable enhancement.</li>
</ul>"""},
            {"id": "cpga-net-plus", "title": "CPGA-Net+: reshaping theoretical illumination", "figures": [
                ("images/Lightweight Image Enhancement/CPGAnet+.webp", "Attention-Based Dynamic Adjustment")],
             "html": """
<p>Detailed in our <em>ArXiv</em> preprint, <strong>CPGA-Net+</strong> extends the framework with
<strong>theoretically-based attentions</strong> for local and global illumination processing. This version
achieves a significant balance between performance and computational cost, effectively addressing the
"theoretical illumination" constraints of previous models.</p>
<p>Code: <a href="https://github.com/Shyandram/CPGA-Net_Plus" target="_blank" rel="noopener">CPGA-Net+ on GitHub</a>.</p>"""},
            {"id": "driving", "title": "Atmospheric scattering for driving scenes", "html": """
<p>Our work presented at <em>IEEE ICCE-TW 2024</em> specifically targets <strong>Exposure Correction</strong> in
dynamic driving scenes. By grounding the enhancement in the atmospheric scattering model, the method improves
object detection accuracy in challenging lighting, from tunnel exits to night driving.</p>"""},
            {"id": "edge-ai", "title": "Side project: edge AI deployment", "html": """
<p>The lightweight nature of these models allows for deployment on resource-constrained hardware:</p>
<ul>
<li><a href="https://github.com/Shyandram/CPGA-Net-IOS" target="_blank" rel="noopener">iOS Implementation</a> (CoreML)</li>
<li><a href="https://github.com/Shyandram/EdgeAI_LLIE-Jetson-Nano.git" target="_blank" rel="noopener">Jetson Nano</a> (TensorRT)</li>
<li><a href="https://github.com/Shyandram/EdgeAI_LLIE_NCS2.git" target="_blank" rel="noopener">Neural Compute Stick 2</a> (OpenVINO)</li>
</ul>"""},
        ],
    },
    {
        "slug": "weather-generation", "featured": False, "category": "generation",
        "title": "Weather Image Generation (Thesis)",
        "title_zh": "用於生成不同天氣影像的端到端深度學習生成網路",
        "year": "2024", "short": "Weather generation",
        "summary": "End-to-End deep learning network using Triplet Content Loss for weather synthesis.",
        "chips": ["Master's Thesis", "Weakly Supervised Learning", "Triplet Content Loss"],
        "card_chips": ["Masters Thesis"],
        "thumb": "images/Weather Image Generation/master_thiesis.webp", "fit": "contain",
        "links": [("Master's Thesis (Chinese)", "https://hdl.handle.net/11296/xjgq5j"),
                  ("English Version", "https://dx.doi.org/10.2139/ssrn.4591716")],
        "facts": [("Type", "Master's Thesis, CYCU"),
                  ("Academic background", "Master of Science in Electronic Engineering (CYCU) & ECE (UWM)")],
        "keywords": ["Data Augmentation", "ADAS Robustness Testing", "Gaming & VR/AR"],
        "sections": [
            {"id": "overview", "title": "Project overview", "figures": [
                ("images/Weather Image Generation/master_thiesis.webp", "Weather Generation Visualization"),
                ("images/Weather Image Generation/master_thiesis_illust.webp", "Network Architecture")], "html": """
<p>This project, conducted as my Master's Thesis, introduces <strong>DGNDW</strong>, an end-to-end deep learning
framework designed to synthesize diverse weather conditions. It addresses the scarcity of adverse weather
datasets (fog, rain, snow) for training robust autonomous driving systems.</p>"""},
            {"id": "techniques", "title": "Core techniques", "html": """
<p>The framework leverages <strong>Weakly Supervised Learning</strong> to translate clear images into
weather-degraded counterparts. A key contribution is the novel <strong>Triplet Content Loss</strong>, which
preserves the semantic structure of the scene while realistically rendering weather effects.</p>
<p>The generated data significantly improves the domain adaptation capabilities of downstream object detectors,
bridging the gap between clear and adverse weather performance.</p>"""},
        ],
    },
    {
        "slug": "dehazing-sr", "featured": False, "category": "restoration",
        "title": "Image Dehazing using SR Networks",
        "title_zh": "除霧與超解析度的串接模型與共同訓練的效益探討以及在物件辨識上之應用",
        "year": "2023", "short": "Dehazing + SR", "award": "Best Paper Award",
        "summary": "Joint training of dehazing and super-resolution models to reduce computation.",
        "chips": ["Best Paper Award", "Image Dehazing", "Super-Resolution"],
        "card_chips": ["Best Paper", "IS3C"],
        "thumb": "images/DHSR/DHSR.webp", "fit": "contain",
        "links": [("IEEE IS3C Paper", "https://ieeexplore.ieee.org/document/10219494")],
        "facts": [("Project type", "Undergraduate Research Excellence"), ("Period", "2023")],
        "keywords": ["Joint Model Training", "Feature Preservation", "Optimized Computation"],
        "sections": [
            {"id": "overview", "title": "Project overview", "figures": [
                ("images/DHSR/DHSR.webp", "Dehazing SR Results")], "html": """
<p>This project explores advanced techniques for <strong>Image Dehazing</strong>, focusing on two key
directions: reducing computational costs through joint super-resolution training and enhancing accuracy using
depth information from stereo and LiDAR systems.</p>"""},
            {"id": "efficient", "title": "Efficient dehazing via super-resolution", "html": """
<p>Awarded the <strong>Best Paper at IEEE IS3C 2023</strong>, this work investigates the synergy between dehazing
and Super-Resolution (SR). By employing a <strong>Joint Training strategy</strong>, we reduce the computational
overhead typically required for high-quality restoration, making it suitable for real-time ADAS
applications.</p>"""},
            {"id": "depth", "title": "Depth-aware dehazing with LiDAR", "html": """
<p>Presented at <strong>IEEE ICASI 2023</strong>, this research leverages <strong>Stereo Depth Estimation
Networks</strong> and <strong>LiDAR-Assisted Cameras</strong>. The fusion of precise depth data helps the model
better estimate haze density (transmission map), leading to cleaner more physically accurate dehazing
results.</p>"""},
        ],
    },
    {
        "slug": "hairstyle-recommendation", "featured": False, "category": "generation",
        "title": "Hairstyle Recommendation System",
        "title_zh": "一個結合臉型分類、換臉和染髮影像處理技術的髮型推薦系統",
        "year": "2023", "short": "Hairstyle recommendation", "award": "1st Place Award",
        "summary": "Face Shape Classification and Swapping for personalized recommendation.",
        "chips": ["1st Place Award", "Face Swapping", "Hair Dyeing"],
        "card_chips": ["1st Place Award", "Conference"],
        "thumb": "images/Hairstyle Recommendation System/hair_recommendation.webp", "fit": "contain",
        "links": [("Conference Article (PDF)",
                   "https://drive.google.com/file/d/1m5GMriR5bY0f0rRyLAGze6_Gpg2QH2Yc/view?usp=sharing")],
        "facts": [("Industry", "Fashion Tech &amp; Intelligent Graphics"), ("Period", "2023")],
        "keywords": ["Face Attribute Analysis", "GAN-based Synthesis", "Image Editing"],
        "sections": [
            {"id": "overview", "title": "Project overview", "figures": [
                ("images/Hairstyle Recommendation System/hair_recommendation.webp", "System Interface")], "html": """
<p>Winner of the <strong>1st Place Award</strong> in the CYCU EL Undergraduate Project Competition, this system
revolutionizes the virtual try-on experience. It provides personalized hairstyle suggestions by integrating
advanced computer vision techniques for facial analysis and image synthesis.</p>"""},
            {"id": "techniques", "title": "Core techniques", "html": """
<p>The core of the recommended system is built upon three advanced modules:</p>
<ul>
<li><strong>Advanced FA (Face Attribute Analysis)</strong>: Precisely classifying face shapes to match suitable
styles.</li>
<li><strong>FS (Face Swapping)</strong>: enabling users to visualize different hairstyles on their own face
realistically.</li>
<li><strong>HDT (Hair Dyeing Transfer)</strong>: Simulating various hair colors to find the perfect look.</li>
</ul>"""},
        ],
    },
    {
        "slug": "drone-survey", "featured": False, "category": "restoration",
        "title": "Drone-based Aerial Image Super-Resolution",
        "title_zh": "以超解析度技術提升無人機載具空拍影像解析度",
        "year": "2022-2023", "short": "Aerial image SR",
        "summary": "Improving the resolution of drone-based aerial images for better object detection.",
        "chips": ["Super-Resolution", "Drone Imaging", "Survey"],
        "card_chips": ["Survey", "UAV"],
        "thumb": "images/SR for Drone-based Aerial Images.webp", "fit": "contain",
        "links": [],
        "facts": [("Role", "Undergraduate Project Leader"), ("Period", "2022-2023")],
        "keywords": ["Drone-based Aerial Images", "Super-Resolution", "Object Detection", "UAV"],
        "sections": [
            {"id": "overview", "title": "Project overview", "figures": [
                ("images/SR for Drone-based Aerial Images.webp", "Drone SR Survey")], "html": """
<p>This project was a comprehensive survey and investigation into improving the resolution of drone-based aerial
images using super-resolution techniques. It served as a subproject of the NSTC-Research Project titled
"Deep Learning-based Multi-Task Super-Resolution Imaging Technology."</p>"""},
            {"id": "focus", "title": "Key focus areas", "html": """
<ul>
<li><strong>UAV Constraints:</strong> Analyzing the limitations of drone hardware and transmission bandwidth.</li>
<li><strong>Small Object Detection:</strong> Improving the detection accuracy of small objects in aerial views
through resolution enhancement.</li>
<li><strong>Real-world Application:</strong> Evaluating the feasibility of deployment on edge devices for
real-time processing.</li>
</ul>"""},
            {"id": "context", "title": "Research context", "html": """
<p>Subproject of NSTC-Research Project: <span lang="zh-TW">基於深度學習的多任務超解析成像技術 - 以衛星、空拍及路側影像應用為例</span></p>"""},
        ],
    },
    {
        "slug": "mask-detection", "featured": False, "category": "detection",
        "title": "Mask Detection &amp; People Flow Systems",
        "title_zh": "基於深度學習網路之口罩配戴辨識",
        "year": "2022-2025", "short": "Mask detection", "award": "Creativity Award",
        "summary": "Real-time public safety monitoring with YOLO-based detection and tracking.",
        "chips": ["Object Detection", "Tracking", "Creativity Award"],
        "card_chips": ["Journal", "Award"],
        "thumb": "images/Mask Detection & People Flow Systems/mask_wearing_cls.webp", "fit": "contain",
        "links": [("Journal Article (PDF)",
                   "https://drive.google.com/file/d/1aH6K4oJzWHm3O7tRLdsa136o_wgOWKWs/view?usp=sharing")],
        "facts": [("Period", "2022-2025"), ("Recognition", "CYCU College Student Research Creativity Award")],
        "keywords": ["YOLO", "DeepSORT", "Deep Learning", "Public Safety Monitoring", "AI for Social Good",
                     "Real-time Surveillance"],
        "sections": [
            {"id": "overview", "title": "Project overview", "figures": [
                ("images/Mask Detection & People Flow Systems/mask_wearing_cls.webp", "Detection Results")],
             "html": """
<p>This project focused on the development of an <strong>Integrated Mask Wearing Classification and People
Counting System</strong> for public health monitoring. Recognized with the <em>CYCU College Student Research
Creativity Award</em>, the system addresses the need for automated compliance checks in public spaces.</p>"""},
            {"id": "techniques", "title": "Core techniques", "html": """
<p>The proposed solution utilizes <strong>YOLOv5s</strong> for high-speed object detection and mask
classification (Correct, Incorrect, None), integrated with <strong>Deep SORT</strong> for robust multi-object
tracking. This combination allows for accurate <strong>Crowd Counting</strong> and individual tracking even in
dense environments.</p>"""},
        ],
    },
]

CATEGORIES = [
    ("all", "All"),
    ("enhancement", "Enhancement"),
    ("restoration", "Restoration & SR"),
    ("detection", "Detection"),
    ("generation", "Generation"),
]
