meta_resources = {
    "Attribute": {
        "Questionnaire.sourceQueries": {
            "type": {"resourceType": "Entity", "id": "Reference"},
            "path": ["sourceQueries"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-sourceQueries",
            "isCollection": True,
        },
        "Questionnaire.launchContext": {
            "path": ["launchContext"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-launchContext",
            "isCollection": True,
        },
        "Questionnaire.launchContext.name": {
            "type": {"resourceType": "Entity", "id": "id"},
            "path": ["launchContext", "name"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "name",
        },
        "Questionnaire.launchContext.type": {
            "type": {"resourceType": "Entity", "id": "code"},
            "path": ["launchContext", "type"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "type",
        },
        "Questionnaire.launchContext.description": {
            "type": {"resourceType": "Entity", "id": "string"},
            "path": ["launchContext", "description"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "description",
        },
        "Questionnaire.item.initialExpression": {
            "type": {"resourceType": "Entity", "id": "Expression"},
            "path": ["item", "initialExpression"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-initialExpression",
        },
        "Questionnaire.itemContext": {
            "type": {"resourceType": "Entity", "id": "Expression"},
            "path": ["itemContext"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-itemContext",
        },
        "Questionnaire.item.itemContext": {
            "type": {"resourceType": "Entity", "id": "Expression"},
            "path": ["item", "itemContext"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-itemContext",
        },
        "Questionnaire.item.hidden": {
            "type": {"resourceType": "Entity", "id": "boolean"},
            "path": ["item", "hidden"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/StructureDefinition/questionnaire-hidden",
        },
        "Questionnaire.mapping": {
            "type": {"resourceType": "Entity", "id": "Reference"},
            "path": ["mapping"],
            "refers": ["Mapping"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://beda.software/fhir-extensions/questionnaire-mapper",
            "isCollection": True,
        },
        "Questionnaire.item.subQuestionnaire": {
            "type": {"resourceType": "Entity", "id": "canonical"},
            "path": ["item", "subQuestionnaire"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "https://jira.hl7.org/browse/FHIR-22356#subQuestionnaire",
        },
        "Questionnaire.assembledFrom": {
            "type": {"resourceType": "Entity", "id": "canonical"},
            "path": ["assembledFrom"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "https://jira.hl7.org/browse/FHIR-22356#assembledFrom",
        },
        "Questionnaire.assembleContext": {
            "path": ["assembleContext"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/uv/sdc/StructureDefinition/sdc-questionnaire-assembleContext",
            "isCollection": True,
        },
        "Questionnaire.assembleContext.name": {
            "type": {"resourceType": "Entity", "id": "id"},
            "path": ["assembleContext", "name"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "name",
        },
        "Questionnaire.assembleContext.type": {
            "type": {"resourceType": "Entity", "id": "code"},
            "path": ["assembleContext", "type"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "type",
        },
        "Questionnaire.assembleContext.description": {
            "type": {"resourceType": "Entity", "id": "string"},
            "path": ["assembleContext", "description"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "description",
        },
        "Questionnaire.item.variable": {
            "type": {"resourceType": "Entity", "id": "Expression"},
            "path": ["item", "variable"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/StructureDefinition/variable",
            "isCollection": True,
        },
        # "Questionnaire.constraint": constraint_extension,
        "Questionnaire.item.constraint": {
            "path": ["item", "constraint"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "http://hl7.org/fhir/StructureDefinition/questionnaire-constraint",
            "isCollection": True,
        },
        "Questionnaire.item.constraint.key": {
            "type": {"resourceType": "Entity", "id": "id"},
            "path": ["item", "constraint", "key"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "key",
            "isRequired": True,
        },
        "Questionnaire.item.constraint.requirements": {
            "type": {"resourceType": "Entity", "id": "string"},
            "path": ["item", "constraint", "requirements"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "requirements",
        },
        "Questionnaire.item.constraint.severity": {
            "type": {"resourceType": "Entity", "id": "code"},
            "path": ["item", "constraint", "severity"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "severity",
            "isRequired": True,
        },
        "Questionnaire.item.constraint.human": {
            "type": {"resourceType": "Entity", "id": "string"},
            "path": ["item", "constraint", "human"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "human",
            "isRequired": True,
        },
        "Questionnaire.item.constraint.location": {
            "type": {"resourceType": "Entity", "id": "string"},
            "path": ["item", "constraint", "location"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "location",
            "isCollection": True,
        },
        "Questionnaire.item.constraint.expression": {
            "type": {"resourceType": "Entity", "id": "Expression"},
            "path": ["item", "constraint", "expression"],
            "resource": {"resourceType": "Entity", "id": "Questionnaire"},
            "extensionUrl": "expression",
            "isRequired": True,
        },
    },
}
