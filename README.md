
<!DOCTYPE html>
<html>
<body>

<h1>Dementia Risk Prediction Platform</h1>

<h2>Overview</h2>
<p>This application employs AWS, SQL, and RShiny to create a comprehensive platform used to predict whether an individual has a high risk of dementia. The project aggregates 180 GB of data to create a detailed view of 180,000 individuals and their potential comorbidities.</p>

<h2>Features</h2>
<ul>
    <li><strong>Data Aggregation</strong>: Compiled data from 180,000 individuals, encompassing a variety of health parameters and potential comorbidities.</li>
    <li><strong>AWS Integration</strong>: Designed an AWS architecture to facilitate cost-effective queries to the database.</li>
    <li><strong>Machine Learning</strong>: Implemented a Random Forest model to combine different parameters and ensure accurate prediction of dementia risk.</li>
    <li><strong>RShiny Interface</strong>: Developed an RShiny application to display results and facilitate queries to the AWS database.</li>
</ul>

<h2>Project Structure</h2>
<ul>
    <li><code>main.py</code>: Contains the Random Forest model and related scripts.</li>
    <li><code>app.py</code>: Contains the RShiny application code.</li>
    <li><code>AlterDataMySQL.py</code>: Includes SQL scripts for database setup and queries.</li>
</ul>

<h2>Setup Instructions</h2>

<h3>Prerequisites</h3>
<ul>
    <li>AWS account with necessary permissions</li>
    <li>R and RShiny installed</li>
    <li>Python installed for running data aggregation and machine learning scripts</li>
    <li>SQL database (e.g., MySQL, PostgreSQL)</li>
</ul>

<h2>Usage</h2>
<ol>
    <li>Open the RShiny application in your web browser.</li>
    <li>Use the interface to input individual health parameters and query the AWS database.</li>
    <li>View the dementia risk prediction results displayed by the RShiny application.</li>
</ol>

<h2>Contributors</h2>
<p><a href="https://github.com/nathanpalamuttam">Nathan Palamuttam</a></p>


<p>For detailed documentation and additional resources, please refer to the individual directories and files within this repository.</p>

</body>
</html>
