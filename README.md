# docker-api-confluence

Documentation de l'API : https://atlassian-python-api.readthedocs.io/en/latest/index.html

## Obtention d'un token

Il faut tout d'abord obtenir un token. Pour cela :
- Rendez-vous sur la page https://id.atlassian.com/manage/api-tokens.
- Cliquez sur Create API token.
- Donnez un nom à votre token (Label = XXX). => atlassian-token
- Cliquez sur Create.
- Cliquez sur Copy to clipboard.

## Configuration

Avant tout, il faut définir trois variables d'environnement utilisées pour s'authentifier sur le site Web Atlassian :

```
export URL=https://XXX.atlassian.net
export API_USERNAME=XXX
export API_PASSWORD=XXX
```

## Confluence

### Création ou modification d'une page Confluence

```
docker run --rm -v $PWD/data:/data -e PARENT="Test" -e SPACE=DEVOPS -e TITLE="Inventaire des projets git" -e FILENAME=myfile -e URL=$URL -e USERNAME=$API_USERNAME -e PASSWORD=$API_PASSWORD api-confluence python /app/create-page.py
```

### Recherche dans les pages Confluence

```
docker run --rm -v $PWD/data:/data -e KEYWORD=certificats -e URL=$URL -e USERNAME=$API_USERNAME -e PASSWORD=$API_PASSWORD api-confluence /app/python search-in-confluence.py
```

```
docker run --rm -v $PWD/data:/data -e SPACE=ADMSYS -e KEYWORD=certificate -e URL=$URL -e USERNAME=$API_USERNAME -e PASSWORD=$API_PASSWORD api-confluence python /app/search-in-confluence-in-a-space.py
```

```
mkdir -p data

cat <<EOF> data/test.cql
siteSearch ~ "It's my keyword" order by created
EOF

docker run --rm -v $PWD/data:/data -e CQL=test.cql -e URL=$URL -e USERNAME=$API_USERNAME -e PASSWORD=$API_PASSWORD api-confluence python /app/run-request-in-confluence.py
```

## Jira

### Création d'un ticket dans Jira

```
docker run --rm -v $PWD/data:/data -e PROJECT="BS" -e ISSUE_TYPE="Story" -e SUMMARY="My summary is here" -e DESCRIPTION=myfile -e URL=$URL -e USERNAME=$API_USERNAME -e PASSWORD=$API_PASSWORD api-confluence python /app/create-ticket.py
```

### Ajout d'un commentaire à un ticket Jira

```
docker run --rm -v $PWD/data:/data -e ISSUE="BS-104" -e COMMENT=myfile -e URL=$URL -e USERNAME=$API_USERNAME -e PASSWORD=$API_PASSWORD api-confluence python /app/add-comment-to-ticket.py
```

```
mkdir -p data

cat <<EOF> data/test.jql
project = PROJ AND status NOT IN (Closed, Resolved) ORDER BY issuekey
EOF

docker run --rm -v $PWD/data:/data -e JQL=test -e URL=$URL -e USERNAME=$API_USERNAME -e PASSWORD=$API_PASSWORD api-confluence python /app/run-request-in-jira.py
```
