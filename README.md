# EgyTech Participants Data (2024)

 This project utilizes a public dataset provided by EgyTech by scraping its API, showcasing data and statistics on participants in the tech industry. This dataset offers valuable insights into various aspects of tech professionals, including job titles, experience levels, compensation, and more.

## Dataset Description

We can unlock the power of data analysis with this dataset, which provides a rich array of information on tech professionals. The data is sourced from EgyTech’s API, enabling users to explore detailed insights into the tech industry landscape.

### Columns Description:

1. **Timestamp (string)**: Date and time of data entry
2. **Gender (string)**: Gender of the participant
3. **Degree (string)**: Indicates if the participant holds a degree in Computer Science (Yes/No)
4. **BusinessMarket (string)**: Indicates the scope of the business market (Global/Regional/Local)
5. **Title (string)**: Job title of the participant
6. **ProgrammingLanguages (string)**: Programming languages known by the participant
7. **BusinessSize (string)**: Size of the participant’s business (Large/Medium/Small)
8. **Yoe (number)**: Years of experience of the participant
9. **YoeBuckets (string)**: Range of years of experience (e.g., “5-8” indicating 5 to 8 years)
10. **BusinessFocus (string)**: Focus of the participant’s business (Product/Software House)
11. **TotalCompensationEgp (number)**: Total compensation in Egyptian pounds
12. **BusinessLine (string)**: Line of business (B2B/B2C/Both)
13. **TotalCompensationEgpBuckets (string)**: Range of total compensation in Egyptian pounds (e.g., “40-50K” indicating 40,000 to 50,000 EGP)
14. **Industries (string)**: Industries associated with the participant’s business
15. **WorkSetting (string)**: Setting of work (e.g., Hybrid)
16. **Level (string)**: Level of the participant’s job (e.g., Mid-level)
17. **IsEgp (string)**: Indicates if the compensation is in Egyptian pounds (Yes/No)
18. **CompanyLocation (string)**: Location of the participant’s company (e.g., Cairo)

## Usage Ideas

- Explore job title distributions and trends in the tech industry.
- Analyze the relationship between experience levels and compensation packages.
- Identify popular programming languages and technologies among tech professionals.
- Investigate regional variations in tech industry demographics and job opportunities.

## How to Use the Code

### Prerequisites

Ensure you have the following Python libraries installed:

- `requests`
- `pandas`

You can install these libraries using pip:

```bash
pip install requests pandas
```
#### Fetching and Analyzing the Data

The provided Python script fetches data from the EgyTech API, processes it, and displays it in a styled DataFrame. Follow these steps:


1.	Clone the Repository

```bash
git clone https://github.com/Mohammed-abdulaziz-eisa/egytech_data_scraper.git
```

2.	Run the Script  

```bash
cd egytech_data_scraper
cd src
python3 scraper.py
```

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

