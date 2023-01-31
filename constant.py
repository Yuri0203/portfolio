import pandas as pd

edu = [['University of Hong Kong (HKU)','Master of Science','Business Analytics','2022','3.8/4.3'],
        ['Beijing Normal University (BNU)','Bachelor of Economics','Finance','2021','3.9/4.0'],
        ['University of Manchester','Sememster Exchange','Finance and Economics', '2020','A+'],
        ['London School of Economics and Political Science','Summer School','Data Science and Machine Learning','2019','A']]

info = {'name':'Yuri Zhang', 
        'Brief':'An analytical and detailed oriented professional with 2+ years of professional experience in business intelligence and data analytics. Conversant with statistical concepts and machine learning techniques. Strong in building data dashboards to report and forecast business performance. Proven ability in crafting engaging stories around data and deriving insights from them. Love to learn new things and ready to face new challenges.', 
        'Email':'zhangyushuangzi@outlook.com',
        'City':'Hong Kong',
        'tableau':'https://public.tableau.com/app/profile/yuri.zhang',
        'edu':pd.DataFrame(edu,columns=['University','Qualification','Major','Year','GPA']),
        'skills':['Business Intelligence', 'Data Visualization','Data Science','Tableau','Tableau Prep','Python','R','SQL','Excel VBA','Power BI','web scraping','A/B Testing'],
        'achievements':['HKU MScBA Merit-based Scholarship, 2022','HKU MScBA Entrance Scholarship, 2021','China National Scholarship, 2018','BNU First-Class Academic Scholarships, 2018 & 2019 & 2020','2nd Prize Winner in Beijing at the 2019 China Undergraduate Mathematical Contest in Modelling (CUMCM)', '2nd Prize Winner at the 2019 Beijing Undergraduate Mathematical Contest in Modelling']}

paper_info = {
        'name':['POI Collection and Brand Identification Enhancement in Indoor Map Production','Employee Attrition Analytics: Turnover Rate Management with Optimal Cost','Credit Card Approval Prediction','Pricing Model for Digital Labor Crowdsourcing Platform'],
        'type':['HKU Business Analytics Capstone Project with Mapxus','Machine Learning & Optimization Project','Machine Learning Project','Mathematical Modelling Project'],
        'year':['2022','2022','2021','2019'],
        'role':['Co-Author','Co-Author','Co-Author','Co-Author'],
        'tool':['Python','Python', 'R', 'MATLAB'],
        'Summary':['',
                'This project aims to apply a predict-then-optimize approach to minimize the HRM cost while retaining an acceptable turnover rate. For the prediction part, Logistics Regression and Random Forest with oversampling are carried out to solve the binary classification problem. Random Forest with 0.5 decision boundary is selected and achieves 83% testing accuracy. For the optimization part, binary optimization problem is formulated and solved with pyomo. Under benchmark analysis and scenario analysis, optimal solution achieves 38% reduction in cost and 63% reduction in turnover rate',
                'This project aims to apply machine learning techniques to help banks detect uncreditworthy applicants who tend to default and reject their applications so as to reduce potential loss. Four methods including Logistic Regression, which is set as the baseline, SVM, Random Forest, and XGBoost, are applied to solve the classification problem. XGBoost with the highest cross-validated-F1 score is selected and used to build the final model. When validated on the testing set, XGBoost achieves near 98% of accuracy.',
                'This project aims to construct an optimal pricing model for a labor crowdsourcing platform to maximize the task completion rate. Firstly, exploratory data analysis, K-means clustering analysis and regression analysis are carried out to understand the factors affecting the finished tasks’ prices. A new pricing model with the objective of balancing the attractiveness of tasks to members is formulated and the optimal solution is obtained by genetic algorithm. The model performance is evaluated by simulating the App’s real-time workflow for new tasks. Finally, a 21% higher task completion rate is achieved. (The report is in Chinese)'],
        'file':['Mapxus.pdf','HR_project.pdf','ML_project.pdf','mathematical_modelling.pdf']}

skill_col_size = 4
embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge" data-locale="en_HK" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="yurizhang99" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/yurizhang99?trk=profile-badge"></a></div>""",
                 'tableau': """<div class='tableauPlaceholder' id='viz1675177348605' style='position: relative'><noscript><a href='#'><img alt='SUPPLIER SCORECARD ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Su&#47;SupplierScorecard_16750932556240&#47;SUPPLIERSCORECARD&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='views&#47;SupplierScorecard_16750932556240&#47;SUPPLIERSCORECARD?:language=en-US&amp;:embed=true' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Su&#47;SupplierScorecard_16750932556240&#47;SUPPLIERSCORECARD&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1675177348605');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} else { vizElement.style.width='100%';vizElement.style.height='3877px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""}


