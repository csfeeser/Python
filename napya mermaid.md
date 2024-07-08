# Network Automation with Python and Ansible (NAPYA)
## Course Content Flowchart

```mermaid
flowchart LR
    subgraph Legend
        direction LR
        classDef day1 fill:#A1C6E7,color:#000000;
        classDef day2 fill:#FAD02E,color:#000000;
        classDef day3 fill:#7FB77E,color:#000000;
        classDef day4 fill:#D46A6A,color:#000000;
        classDef day5 fill:#9E9E9E,color:#000000;
        
        D1[Day 1]:::day1
        D2[Day 2]:::day2
        D3[Day 3]:::day3
        D4[Day 4]:::day4
        D5[Day 5]:::day5
    end
    
    subgraph s1["PYTHON"]
        direction LR
        classDef title fill:#ffffff,stroke:none,font-size:18px,align:left;
        class s1 title;

        WC["Writing Custom Modules"]:::day5
        UNPW["UN/PW"]:::day3
        RSA["RSA Keys"]:::day3
        PM["Paramiko"]:::day3
        M["Methods"]:::day1
        RL["Requests Library"]:::day2
        D["Dictionaries"]:::day1
        L["Lists"]:::day1
        DT["Data Types"]:::day1
        BIF["Built-in Functions"]:::day1
        PF["Python Fundamentals"]:::day1
        S["Scripts"]:::day3
    end
    
    PF --> BIF
    BIF --> M
    BIF --> DT
    DT --> L
    DT --> D
    DT --> S
    M --> DT
    L --> JSON:::day2
    D --> JSON
    JSON --> RAPI["RESTful APIs"]:::day2
    RAPI --> RL
    NA["Network Automation"]:::day3 --> PM
    PM --> RSA
    PM --> UNPW
    S --> NA
    
    subgraph s2["ANSIBLE"]
        direction LR
        classDef title fill:#ffffff,stroke:none,font-size:18px,align:left;
        class s2 title;

        VA["Vendor Agnostic"]:::day4
        VS["Vendor Specific"]:::day4
        NM["Networking Modules"]:::day4
        Scr["Script"]:::day5
        Cl["Collections"]:::day3
        Wh["When"]:::day2
        Reg["Register"]:::day2
        Lp["Looping"]:::day2
        KW["Keywords"]:::day2
        LP["Lookup Plugins"]:::day5
        JF["Jinja2 Filters"]:::day5
        Tpl["Template"]:::day5
        Raw:::day3
        Uri:::day2
        Dbg["Debug"]:::day2
        AV["Ansible Vault"]:::day5
        VP["Vars Prompt"]:::day5
        R["Roles"]:::day4
        Sec["Security"]:::day5
        AR["Ansible Runner"]:::day4
        PC["Prechecks"]:::day3
        EH["Error Handling"]:::day3
        PD["Playbook Design"]:::day3
        ACT["Ansible Connection Types"]:::day4
        MOD["Modules"]:::day1
        PP["Playbook Parts"]:::day1
        AF["Ansible Fundamentals"]:::day1
    end
    
    AF --> PP
    PP --> MOD
    MOD --> Dbg
    MOD --> Uri
    Uri --> RAPI
    MOD --> Raw
    MOD --> Tpl
    Tpl --> JF
    JF --> LP
    MOD --> KW
    KW --> Lp
    KW --> Reg
    KW --> Wh
    MOD --> Cl
    Cl --> WC
    MOD --> Scr
    MOD --> NA
    NA --> NM
    NM --> VS
    NM --> VA
    PP --> ACT
    ACT --> AR
    PP --> PD
    PD --> EH
    EH --> PC
    PD --> Sec
    Sec --> VP
    Sec --> AV
    PD --> R

```
