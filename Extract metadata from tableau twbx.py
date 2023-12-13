import zipfile
import xml.etree.ElementTree as ET

def extract_data_source_info(twbx_file_path):
    # Open the .twbx file as a ZIP archive
    with zipfile.ZipFile(twbx_file_path, 'r') as zip_file:
        # Find the workbook XML file within the archive
        workbook_xml_path = None
        for file_info in zip_file.infolist():
            if file_info.filename.endswith('.twb'):
                workbook_xml_path = file_info.filename
                break

        if not workbook_xml_path:
            raise Exception("Workbook XML not found in the .twbx file.")

        # Extract the workbook XML content
        with zip_file.open(workbook_xml_path) as xml_file:
            xml_content = xml_file.read()

        # Parse the workbook XML
        root = ET.fromstring(xml_content)

        # Extract data source information
        data_sources = root.findall('.//connection')
        for data_source in data_sources:
            connection_attributes = data_source.attrib
            data_source_name = connection_attributes.get('dbname', '')
            table_name = connection_attributes.get('table', '')
            schema_name = connection_attributes.get('schema', '')

            print(f"Data Source: {data_source_name}, Table: {table_name}, Schema: {schema_name}")

# Provide the path to your .twbx file
twbx_file_path = r"file location"

# Call the function to extract data source information
extract_data_source_info(twbx_file_path)
