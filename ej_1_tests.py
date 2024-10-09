from ej_1 import main as mainEjercicio1


def getNombres(influencers):
    nombres = []
    for influencer in influencers:
        nombres.append(influencer["nombre"])
    return nombres


def test01ArchivoDeLaConsigna(resultadoTests):
    print("══════════════════════════════════════════════")
    try:
        filename = "./ej_1_test_files/1.csv"
        mejorLista, valorMejorLista = mainEjercicio1(filename)

        assert ["Pucho", "Tucho", "Suncho", "Fercho"] == getNombres(mejorLista)
        assert 89 == valorMejorLista
    except:
        print("No Pasó ❌ Test 01 'test01ArchivoDeLaConsigna'")
        resultadoTests["noPasaron"] += 1
        return

    print("Pasó ✅ Test 01 'test01ArchivoDeLaConsigna'")
    resultadoTests["pasaron"] += 1


def test02ArchivoDeLaConsignaShuffled1(resultadoTests):
    print("══════════════════════════════════════════════")
    try:
        filename = "./ej_1_test_files/2.csv"
        mejorLista, valorMejorLista = mainEjercicio1(filename)

        assert ["Pucho", "Tucho", "Suncho", "Fercho"] == getNombres(mejorLista)
        assert 89 == valorMejorLista
    except:
        print("No Pasó ❌ Test 02 'test02ArchivoDeLaConsignaShuffled1'")
        resultadoTests["noPasaron"] += 1
        return

    print("Pasó ✅ Test 02 'test02ArchivoDeLaConsignaShuffled1'")
    resultadoTests["pasaron"] += 1


def test03ArchivoDeLaConsignaShuffled2(resultadoTests):
    print("══════════════════════════════════════════════")
    try:
        filename = "./ej_1_test_files/3.csv"
        mejorLista, valorMejorLista = mainEjercicio1(filename)

        assert ["Pucho", "Tucho", "Suncho", "Fercho"] == getNombres(mejorLista)
        assert 89 == valorMejorLista
    except:
        print("No Pasó ❌ Test 03 'test03ArchivoDeLaConsignaShuffled2'")
        resultadoTests["noPasaron"] += 1
        return

    print("Pasó ✅ Test 03 'test03ArchivoDeLaConsignaShuffled2'")
    resultadoTests["pasaron"] += 1


def test04ArchivoDeLaConsignaShuffled3(resultadoTests):
    print("══════════════════════════════════════════════")
    try:
        filename = "./ej_1_test_files/4.csv"
        mejorLista, valorMejorLista = mainEjercicio1(filename)

        assert ["Pucho", "Tucho", "Suncho", "Fercho"] == getNombres(mejorLista)
        assert 89 == valorMejorLista
    except:
        print("No Pasó ❌ Test 04 'test04ArchivoDeLaConsignaShuffled3'")
        resultadoTests["noPasaron"] += 1
        return

    print("Pasó ✅ Test 04 'test04ArchivoDeLaConsignaShuffled3'")
    resultadoTests["pasaron"] += 1


def test05ArchivoVacio(resultadoTests):
    print("══════════════════════════════════════════════")
    try:
        filename = "./ej_1_test_files/5.csv"
        mejorLista, valorMejorLista = mainEjercicio1(filename)

        assert [] == getNombres(mejorLista)
        assert 0 == valorMejorLista
    except:
        print("No Pasó ❌ Test 05 'test05ArchivoVacio'")
        resultadoTests["noPasaron"] += 1
        return

    print("Pasó ✅ Test 05 'test05ArchivoVacio'")
    resultadoTests["pasaron"] += 1


def test06Archivo1Influencer(resultadoTests):
    print("══════════════════════════════════════════════")
    try:
        filename = "./ej_1_test_files/6.csv"
        mejorLista, valorMejorLista = mainEjercicio1(filename)

        assert ["Lucho"] == getNombres(mejorLista)
        assert 10 == valorMejorLista
    except:
        print("No Pasó ❌ Test 06 'test06Archivo1Influencer'")
        resultadoTests["noPasaron"] += 1
        return

    print("Pasó ✅ Test 06 'test06Archivo1Influencer'")
    resultadoTests["pasaron"] += 1


def test07Archivo2Influencers(resultadoTests):
    print("══════════════════════════════════════════════")
    try:
        filename = "./ej_1_test_files/7.csv"
        mejorLista, valorMejorLista = mainEjercicio1(filename)

        assert ["Pucho", "Suncho"] == getNombres(mejorLista)
        assert 55 == valorMejorLista
    except:
        print("No Pasó ❌ Test 07 'test07Archivo2Influencers'")
        resultadoTests["noPasaron"] += 1
        return

    print("Pasó ✅ Test 07 'test07Archivo2Influencers'")
    resultadoTests["pasaron"] += 1


def test08ArchivoMuchosInfluencers1ConMuchaIncompatibilidad(resultadoTests):
    print("══════════════════════════════════════════════")
    try:
        filename = "./ej_1_test_files/8.csv"
        mejorLista, valorMejorLista = mainEjercicio1(filename)

        assert ["Alice", "Dave"] == getNombres(mejorLista)
        assert 140 == valorMejorLista
    except:
        print(
            "No Pasó ❌ Test 08 'test08ArchivoMuchosInfluencers1ConMuchaIncompatibilidad'"
        )
        resultadoTests["noPasaron"] += 1
        return

    print("Pasó ✅ Test 08 'test08ArchivoMuchosInfluencers1ConMuchaIncompatibilidad'")
    resultadoTests["pasaron"] += 1


def test09ArchivoTodosSonIncompatibles(resultadoTests):
    print("══════════════════════════════════════════════")
    try:
        filename = "./ej_1_test_files/9.csv"
        mejorLista, valorMejorLista = mainEjercicio1(filename)

        assert ["Pucho"] == getNombres(mejorLista)
        assert 40 == valorMejorLista
    except:
        print("No Pasó ❌ Test 09 'test09ArchivoTodosSonIncompatibles'")
        resultadoTests["noPasaron"] += 1
        return

    print("Pasó ✅ Test 09 'test09ArchivoTodosSonIncompatibles'")
    resultadoTests["pasaron"] += 1


def test10ArchivoEjemploSimpleDelInforme(resultadoTests):
    print("══════════════════════════════════════════════")
    try:
        filename = "./ej_1_test_files/10.csv"
        mejorLista, valorMejorLista = mainEjercicio1(filename)

        assert ["Gabriel", "Pedro"] == getNombres(mejorLista)
        assert 16 == valorMejorLista
    except:
        print("No Pasó ❌ Test 10 'test10ArchivoEjemploSimpleDelInforme'")
        resultadoTests["noPasaron"] += 1
        return

    print("Pasó ✅ Test 10 'test10ArchivoEjemploSimpleDelInforme'")
    resultadoTests["pasaron"] += 1


if __name__ == "__main__":
    resultadoTests = {"pasaron": 0, "noPasaraon": 0}

    test01ArchivoDeLaConsigna(resultadoTests)
    test02ArchivoDeLaConsignaShuffled1(resultadoTests)
    test03ArchivoDeLaConsignaShuffled2(resultadoTests)
    test04ArchivoDeLaConsignaShuffled3(resultadoTests)
    test05ArchivoVacio(resultadoTests)
    test06Archivo1Influencer(resultadoTests)
    test07Archivo2Influencers(resultadoTests)
    test08ArchivoMuchosInfluencers1ConMuchaIncompatibilidad(resultadoTests)
    test09ArchivoTodosSonIncompatibles(resultadoTests)
    test10ArchivoEjemploSimpleDelInforme(resultadoTests)

    print("══════════════════════════════════════════════")
    print(
        f"Pasaron {resultadoTests['pasaron']} tests. Fallaron {resultadoTests['noPasaraon']} tests."
    )
