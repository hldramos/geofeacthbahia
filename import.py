import requests
import json

URL = "https://raw.githubusercontent.com/tbrugz/geodata-br/master/geojson/geojs-29-mun.json"


def filtrar_geojson_por_ids(
    lista_ids, arquivo_saida="resultado.geojson", campos_id=None
):
    if campos_id is None:
        campos_id = ["id", "ID", "cod_ibge", "codigo_ibge", "CD_GEOCMU"]

    ids_desejados = {str(i) for i in lista_ids}

    response = requests.get(URL, timeout=60)
    response.raise_for_status()
    geojson = response.json()

    features_encontradas = []

    for feature in geojson.get("features", []):
        props = feature.get("properties", {})

        for campo in campos_id:
            valor = props.get(campo)
            if valor is not None and str(valor) in ids_desejados:
                features_encontradas.append(feature)
                break

    resultado = {"type": "FeatureCollection", "features": features_encontradas}

    with open(arquivo_saida, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)

    return {
        "total_ids_informados": len(lista_ids),
        "total_encontrados": len(features_encontradas),
        "arquivo_saida": arquivo_saida,
    }


# Exemplo de uso
ids = [
    "2900108",
    "2901304",
    "2902609",
    "2902807",
    "2903003",
    "2903235",
    "2903805",
    "2904001",
    "2904050",
    "2904100",
    "2904506",
    "2905305",
    "2906204",
    "2909802",
    "2910800",
    "2912202",
    "2912400",
    "2912509",
    "2912608",
    "2913002",
    "2913101",
    "2913200",
    "2914109",
    "2914307",
    "2914406",
    "2914604",
    "2914703",
    "2915007",
    "2917607",
    "2918506",
    "2918605",
    "2919009",
    "2919157",
    "2919306",
    "2919553",
    "2919603",
    "2919801",
    "2920452",
    "2920502",
    "2920809",
    "2921609",
    "2921708",
    "2921906",
    "2922052",
    "2922102",
    "2922250",
    "2922854",
    "2923035",
    "2923209",
    "2923407",
    "2923506",
    "2923605",
    "2923704",
    "2924306",
    "2925808",
    "2925956",
    "2926707",
    "2926905",
    "2927200",
    "2927408",
    "2928505",
    "2929909",
    "2930204",
    "2930808",
    "2930907",
    "2931053",
    "2931103",
    "2932804",
    "2933174",
    "2933406",
    "2933604",
]

retorno = filtrar_geojson_por_ids(ids, "calcario.geojson")
print(retorno)
