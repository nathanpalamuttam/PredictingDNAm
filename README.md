
<!DOCTYPE html>
<html>
<head>
    <title>Dementia Risk Prediction Platform</title>
</head>
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
    <li><code>data/</code>: Contains the aggregated data files.</li>
    <li><code>aws/</code>: Includes scripts and configuration files for setting up the AWS environment.</li>
    <li><code>models/</code>: Contains the Random Forest model and related scripts.</li>
    <li><code>rshiny/</code>: Contains the RShiny application code.</li>
    <li><code>sql/</code>: Includes SQL scripts for database setup and queries.</li>
</ul>

<h2>Setup Instructions</h2>

<h3>Prerequisites</h3>
<ul>
    <li>AWS account with necessary permissions</li>
    <li>R and RShiny installed</li>
    <li>Python installed for running data aggregation and machine learning scripts</li>
    <li>SQL database (e.g., MySQL, PostgreSQL)</li>
</ul>

<h3>AWS Setup</h3>
<ol>
    <li>Navigate to the <code>aws/</code> directory.</li>
    <li>Follow the instructions in <code>aws_setup.md</code> to configure the AWS environment.</li>
    <li>Deploy the necessary AWS resources using the provided CloudFormation template or manual setup instructions.</li>
</ol>

<h3>Data Aggregation</h3>
<ol>
    <li>Place the raw data files in the <code>data/raw/</code> directory.</li>
    <li>Run the data aggregation script:
        <pre><code>python data/aggregate_data.py</code></pre>
    </li>
    <li>The aggregated data will be saved in <code>data/processed/</code>.</li>
</ol>

<h3>SQL Database</h3>
<ol>
    <li>Set up the SQL database using the scripts in the <code>sql/</code> directory.</li>
    <li>Load the aggregated data into the database:
        <pre><code>python sql/load_data.py</code></pre>
    </li>
</ol>

<h3>Machine Learning Model</h3>
<ol>
    <li>Train the Random Forest model:
        <pre><code>python models/train_model.py</code></pre>
    </li>
    <li>Save the trained model in the <code>models/saved/</code> directory.</li>
</ol>

<h3>RShiny Application</h3>
<ol>
    <li>Navigate to the <code>rshiny/</code> directory.</li>
    <li>Run the RShiny application:
        <pre><code>shiny::runApp()</code></pre>
    </li>
</ol>

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
