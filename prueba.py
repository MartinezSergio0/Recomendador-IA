
import pandas as pd

df = pd.read_csv('dataPrueba.csv')

# Etiquetado manual por marca y modelo
# Basado en conocimiento real del mercado automotriz

etiquetas = {}

# ── ACURA ─────────────────────────────────────────────────────────
etiquetas[('ACURA', 'VIGOR')]            = 'lujo_sedan'       # Sedán premium 90s
etiquetas[('ACURA', 'LEGEND')]           = 'lujo_sedan'       # Sedán flagship Acura
etiquetas[('ACURA', 'SLX')]              = 'lujo_suv'         # SUV badge-engineered de Isuzu, vendido como lujo
etiquetas[('ACURA', 'INTEGRA')]          = 'deportivo'        # Hatchback deportivo icónico
etiquetas[('ACURA', 'RSX')]              = 'deportivo'        # Sucesor del Integra, coupe deportivo
etiquetas[('ACURA', 'CL')]               = 'lujo_sedan'       # Coupe premium Acura
etiquetas[('ACURA', 'ILX')]              = 'lujo_sedan'       # Entry-level Acura
etiquetas[('ACURA', 'ILX HYBRID')]       = 'lujo_sedan'       # Versión híbrida, mismo segmento
etiquetas[('ACURA', 'TSX')]              = 'lujo_sedan'       # Sedán compacto premium
etiquetas[('ACURA', 'TSX SPORT WAGON')]  = 'lujo_sedan'       # Wagon premium
etiquetas[('ACURA', 'TLX')]              = 'lujo_sedan'       # Sedán mediano premium
etiquetas[('ACURA', 'RDX')]              = 'lujo_suv'         # SUV compacto premium
etiquetas[('ACURA', 'TL')]               = 'lujo_sedan'       # Sedán premium clásico
etiquetas[('ACURA', 'MDX')]              = 'lujo_suv'         # SUV 3 filas premium
etiquetas[('ACURA', 'ZDX')]              = 'lujo_suv'         # SUV coupe premium
etiquetas[('ACURA', 'RL')]               = 'lujo_sedan'       # Flagship sedán
etiquetas[('ACURA', 'RLX')]              = 'lujo_sedan'       # Sucesor del RL
etiquetas[('ACURA', 'NSX')]              = 'deportivo'        # Superdeportivo icónico, no hiper_lujo

# ── ALFA ROMEO ────────────────────────────────────────────────────
etiquetas[('ALFA ROMEO', '4C')]          = 'deportivo'        # Coupe deportivo RWD puro

# ── ASTON MARTIN ──────────────────────────────────────────────────
# Toda la línea Aston Martin es hiper_lujo — mínimo $129k, marca exclusiva
for model in ['V8 VANTAGE','DB7','V12 VANTAGE','V12 VANTAGE S','DB9',
              'RAPIDE S','RAPIDE','DB9 GT','VIRAGE','V12 VANQUISH','DBS','VANQUISH']:
    etiquetas[('ASTON MARTIN', model)] = 'hiper_lujo'

# ── AUDI ──────────────────────────────────────────────────────────
etiquetas[('AUDI', '100')]               = 'lujo_sedan'       # Sedán premium europeo 90s
etiquetas[('AUDI', '200')]               = 'lujo_sedan'       # Versión tope del 100
etiquetas[('AUDI', '80')]                = 'lujo_sedan'       # Sedán compacto premium
etiquetas[('AUDI', '90')]                = 'lujo_sedan'       # Sedán compacto premium
etiquetas[('AUDI', 'COUPE')]             = 'deportivo'        # Coupe Quattro clásico
etiquetas[('AUDI', 'V8')]                = 'lujo_sedan'       # Flagship sedán Audi 90s
etiquetas[('AUDI', 'CABRIOLET')]         = 'deportivo'        # Convertible premium
etiquetas[('AUDI', 'Q3')]                = 'lujo_suv'         # SUV compacto premium
etiquetas[('AUDI', 'A3')]                = 'lujo_sedan'       # Entry premium Audi
etiquetas[('AUDI', 'A4')]                = 'lujo_sedan'       # Sedán premium mediano
etiquetas[('AUDI', 'ALLROAD QUATTRO')]   = 'lujo_sedan'       # Wagon aventurero premium
etiquetas[('AUDI', 'TT')]                = 'deportivo'        # Coupe/convertible deportivo icónico
etiquetas[('AUDI', 'A5')]                = 'deportivo'        # Coupe premium deportivo
etiquetas[('AUDI', 'ALLROAD')]           = 'lujo_sedan'       # Wagon AWD premium
etiquetas[('AUDI', 'S3')]                = 'deportivo'        # Versión S = performance
etiquetas[('AUDI', 'A4 ALLROAD')]        = 'lujo_sedan'       # Wagon premium AWD
etiquetas[('AUDI', 'Q5')]                = 'lujo_suv'         # SUV mediano premium
etiquetas[('AUDI', 'TTS')]               = 'deportivo'        # TT S = más deportivo aún
etiquetas[('AUDI', 'S4')]                = 'deportivo'        # Sedán de alto rendimiento
etiquetas[('AUDI', 'A6')]                = 'lujo_sedan'       # Sedán ejecutivo
etiquetas[('AUDI', 'SQ5')]               = 'lujo_suv'         # SUV performance premium
etiquetas[('AUDI', 'TT RS')]             = 'deportivo'        # RS = máximo rendimiento TT
etiquetas[('AUDI', 'Q7')]                = 'lujo_suv'         # SUV grande premium
etiquetas[('AUDI', 'S5')]                = 'deportivo'        # Coupe performance
etiquetas[('AUDI', 'A7')]                = 'lujo_sedan'       # Fastback ejecutivo
etiquetas[('AUDI', 'RS 4')]              = 'deportivo'        # RS = máximo rendimiento
etiquetas[('AUDI', 'S6')]                = 'deportivo'        # Sedán alto rendimiento
etiquetas[('AUDI', 'RS 5')]              = 'deportivo'        # Convertible alto rendimiento
etiquetas[('AUDI', 'S7')]                = 'deportivo'        # Fastback performance
etiquetas[('AUDI', 'RS 6')]              = 'deportivo'        # Wagon performance
etiquetas[('AUDI', 'A8')]                = 'lujo_sedan'       # Flagship sedán Audi
etiquetas[('AUDI', 'RS 7')]              = 'deportivo'        # Fastback máximo rendimiento
etiquetas[('AUDI', 'S8')]                = 'deportivo'        # Sedan flagship performance
etiquetas[('AUDI', 'R8')]                = 'hiper_lujo'       # Superdeportivo >$150k, mid-engine

# ── BENTLEY ───────────────────────────────────────────────────────
# Toda la línea Bentley es hiper_lujo sin excepción
for model in ['CONTINENTAL FLYING SPUR','FLYING SPUR','CONTINENTAL GTC',
              'CONTINENTAL FLYING SPUR SPEED','CONTINENTAL GT SPEED','CONTINENTAL GT',
              'CONTINENTAL GTC SPEED','CONTINENTAL GT SPEED CONVERTIBLE','ARNAGE',
              'CONTINENTAL SUPERSPORTS','CONTINENTAL SUPERSPORTS CONVERTIBLE',
              'SUPERSPORTS CONVERTIBLE ISR','CONTINENTAL','MULSANNE','AZURE',
              'CONTINENTAL GT3-R','BROOKLANDS','AZURE T']:
    etiquetas[('BENTLEY', model)] = 'hiper_lujo'

# ── BMW ───────────────────────────────────────────────────────────
etiquetas[('BMW', '8 SERIES')]           = 'deportivo'        # Gran Turismo coupe premium
etiquetas[('BMW', 'Z3')]                 = 'deportivo'        # Roadster clásico
etiquetas[('BMW', 'X1')]                 = 'lujo_suv'         # SUV compacto entry premium
etiquetas[('BMW', '1 SERIES')]           = 'deportivo'        # Coupe/conv compacto RWD
etiquetas[('BMW', '3 SERIES')]           = 'lujo_sedan'       # Sedán premium mediano icónico
etiquetas[('BMW', '2 SERIES')]           = 'deportivo'        # Coupe compacto RWD
etiquetas[('BMW', 'X3')]                 = 'lujo_suv'         # SUV compacto premium
etiquetas[('BMW', 'I3')]                 = 'compacto_urbano'  # Eléctrico urbano, diseño city-car
etiquetas[('BMW', '4 SERIES GRAN COUPE')]= 'lujo_sedan'       # Fastback premium 4 puertas
etiquetas[('BMW', '3 SERIES GRAN TURISMO')]= 'lujo_sedan'     # Hatchback premium familiar
etiquetas[('BMW', '1 SERIES M')]         = 'deportivo'        # M = máximo rendimiento
etiquetas[('BMW', 'M')]                  = 'deportivo'        # M Coupe clásico
etiquetas[('BMW', '4 SERIES')]           = 'deportivo'        # Coupe mediano premium
etiquetas[('BMW', 'X4')]                 = 'lujo_suv'         # SUV coupe premium
etiquetas[('BMW', 'Z4 M')]               = 'deportivo'        # Roadster M performance
etiquetas[('BMW', 'M2')]                 = 'deportivo'        # Coupe compacto M
etiquetas[('BMW', 'Z4')]                 = 'deportivo'        # Roadster premium
etiquetas[('BMW', '5 SERIES')]           = 'lujo_sedan'       # Sedán ejecutivo clásico
etiquetas[('BMW', 'X5')]                 = 'lujo_suv'         # SUV mediano premium referente
etiquetas[('BMW', 'ACTIVEHYBRID 5')]     = 'lujo_sedan'       # 5 Series híbrido
etiquetas[('BMW', 'M3')]                 = 'deportivo'        # M3 — icono del sedán deportivo
etiquetas[('BMW', '5 SERIES GRAN TURISMO')]= 'lujo_sedan'     # 5 GT hatchback premium
etiquetas[('BMW', 'X6')]                 = 'lujo_suv'         # SUV coupe premium
etiquetas[('BMW', 'M4')]                 = 'deportivo'        # Coupe M performance
etiquetas[('BMW', 'ACTIVEHYBRID 7')]     = 'lujo_sedan'       # 7 Series híbrido
etiquetas[('BMW', '6 SERIES GRAN COUPE')]= 'lujo_sedan'       # Gran coupe ejecutivo
etiquetas[('BMW', '6 SERIES')]           = 'deportivo'        # Gran Turismo convertible
etiquetas[('BMW', 'ACTIVEHYBRID X6')]    = 'lujo_suv'         # X6 híbrido
etiquetas[('BMW', '7 SERIES')]           = 'lujo_sedan'       # Flagship sedán
etiquetas[('BMW', 'M5')]                 = 'deportivo'        # Sedán M máximo rendimiento
etiquetas[('BMW', 'X5 M')]               = 'lujo_suv'         # SUV M performance
etiquetas[('BMW', 'X6 M')]               = 'lujo_suv'         # SUV coupe M
etiquetas[('BMW', 'M6')]                 = 'deportivo'        # Coupe/conv M flagship
etiquetas[('BMW', 'M6 GRAN COUPE')]      = 'deportivo'        # Gran coupe M
etiquetas[('BMW', 'ALPINA B6 GRAN COUPE')]= 'hiper_lujo'      # Alpina >$120k, ultra exclusivo
etiquetas[('BMW', 'Z8')]                 = 'hiper_lujo'       # Roadster coleccionista $130k
etiquetas[('BMW', 'ALPINA B7')]          = 'hiper_lujo'       # Alpina flagship $132k
etiquetas[('BMW', 'M4 GTS')]             = 'hiper_lujo'       # Edición limitada $133k
etiquetas[('BMW', 'ALPINA')]             = 'hiper_lujo'       # Alpina convertible $137k

# ── BUGATTI ───────────────────────────────────────────────────────
etiquetas[('BUGATTI', 'VEYRON 16.4')]    = 'hiper_lujo'       # $1.7M, el auto más caro del dataset

# ── BUICK ─────────────────────────────────────────────────────────
etiquetas[('BUICK', 'ELECTRA')]          = 'sedan_familiar'   # Sedán grande americano 90s
etiquetas[('BUICK', 'ESTATE WAGON')]     = 'sedan_familiar'   # Wagon familiar clásico
etiquetas[('BUICK', 'REATTA')]           = 'deportivo'        # Coupe/conv sportivo Buick
etiquetas[('BUICK', 'SKYLARK')]          = 'compacto_urbano'  # Sedán compacto accesible
etiquetas[('BUICK', 'ROADMASTER')]       = 'sedan_familiar'   # Sedán grande americano
etiquetas[('BUICK', 'RIVIERA')]          = 'deportivo'        # Coupe personal luxury
etiquetas[('BUICK', 'CENTURY')]          = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('BUICK', 'VERANO')]           = 'lujo_sedan'       # Sedán compacto premium
etiquetas[('BUICK', 'RENDEZVOUS')]       = 'suv_familiar'     # SUV familiar accesible
etiquetas[('BUICK', 'ENCORE')]           = 'lujo_suv'         # SUV compacto premium
etiquetas[('BUICK', 'LESABRE')]          = 'sedan_familiar'   # Sedán grande americano
etiquetas[('BUICK', 'TERRAZA')]          = 'sedan_familiar'   # Minivan familiar
etiquetas[('BUICK', 'REGAL')]            = 'lujo_sedan'       # Sedán premium mediano
etiquetas[('BUICK', 'RAINIER')]          = 'suv_familiar'     # SUV mediano
etiquetas[('BUICK', 'LUCERNE')]          = 'lujo_sedan'       # Sedán grande premium
etiquetas[('BUICK', 'CASCADA')]          = 'deportivo'        # Convertible premium
etiquetas[('BUICK', 'LACROSSE')]         = 'lujo_sedan'       # Sedán premium
etiquetas[('BUICK', 'PARK AVENUE')]      = 'lujo_sedan'       # Flagship sedán Buick
etiquetas[('BUICK', 'ENVISION')]         = 'lujo_suv'         # SUV mediano premium
etiquetas[('BUICK', 'ENCLAVE')]          = 'lujo_suv'         # SUV grande premium

# ── CADILLAC ──────────────────────────────────────────────────────
etiquetas[('CADILLAC', 'BROUGHAM')]      = 'lujo_sedan'       # Sedán grande lujo americano
etiquetas[('CADILLAC', 'SIXTY SPECIAL')] = 'lujo_sedan'       # Flagship Cadillac 90s
etiquetas[('CADILLAC', 'FLEETWOOD')]     = 'lujo_sedan'       # Limousine/sedán lujo
etiquetas[('CADILLAC', 'ALLANTE')]       = 'deportivo'        # Convertible lujo/deportivo
etiquetas[('CADILLAC', 'CATERA')]        = 'lujo_sedan'       # Sedán mediano lujo
etiquetas[('CADILLAC', 'ELDORADO')]      = 'deportivo'        # Coupe personal luxury
etiquetas[('CADILLAC', 'ATS')]           = 'lujo_sedan'       # Sedán compacto premium
etiquetas[('CADILLAC', 'CTS COUPE')]     = 'deportivo'        # Coupe performance premium
etiquetas[('CADILLAC', 'CTS WAGON')]     = 'lujo_sedan'       # Wagon premium
etiquetas[('CADILLAC', 'ATS COUPE')]     = 'deportivo'        # Coupe compacto premium
etiquetas[('CADILLAC', 'SRX')]           = 'lujo_suv'         # SUV mediano premium
etiquetas[('CADILLAC', 'SEVILLE')]       = 'lujo_sedan'       # Sedán lujo clásico
etiquetas[('CADILLAC', 'DEVILLE')]       = 'lujo_sedan'       # Flagship Cadillac
etiquetas[('CADILLAC', 'XT5')]           = 'lujo_suv'         # SUV mediano premium moderno
etiquetas[('CADILLAC', 'DTS')]           = 'lujo_sedan'       # Sedán grande lujo
etiquetas[('CADILLAC', 'STS')]           = 'lujo_sedan'       # Sedán mediano lujo
etiquetas[('CADILLAC', 'CTS')]           = 'lujo_sedan'       # Sedán mediano premium
etiquetas[('CADILLAC', 'XTS')]           = 'lujo_sedan'       # Sedán grande premium
etiquetas[('CADILLAC', 'ATS-V')]         = 'deportivo'        # Coupe V = alto rendimiento
etiquetas[('CADILLAC', 'CTS-V WAGON')]   = 'deportivo'        # Wagon V performance
etiquetas[('CADILLAC', 'CTS-V COUPE')]   = 'deportivo'        # Coupe V performance
etiquetas[('CADILLAC', 'CT6')]           = 'lujo_sedan'       # Flagship moderno
etiquetas[('CADILLAC', 'ESCALADE EXT')]  = 'aventura_pickup'  # Pickup basado en Escalade
etiquetas[('CADILLAC', 'CTS-V')]         = 'deportivo'        # Sedán V máximo rendimiento
etiquetas[('CADILLAC', 'STS-V')]         = 'deportivo'        # Sedán V performance
etiquetas[('CADILLAC', 'ESCALADE HYBRID')]= 'lujo_suv'        # Escalade híbrido
etiquetas[('CADILLAC', 'ESCALADE')]      = 'lujo_suv'         # SUV grande lujo icónico
etiquetas[('CADILLAC', 'XLR')]           = 'deportivo'        # Roadster lujo
etiquetas[('CADILLAC', 'ESCALADE ESV')]  = 'lujo_suv'         # Escalade extendido
etiquetas[('CADILLAC', 'XLR-V')]         = 'hiper_lujo'       # Roadster V $100k+ performance

# ── CHEVROLET ─────────────────────────────────────────────────────
etiquetas[('CHEVROLET', 'BERETTA')]      = 'compacto_urbano'  # Coupe compacto accesible
etiquetas[('CHEVROLET', 'CAPRICE')]      = 'sedan_familiar'   # Sedán grande americano
etiquetas[('CHEVROLET', 'CELEBRITY')]    = 'sedan_familiar'   # Wagon familiar
etiquetas[('CHEVROLET', 'CORSICA')]      = 'compacto_urbano'  # Sedán compacto básico
etiquetas[('CHEVROLET', 'S-10 BLAZER')]  = 'suv_familiar'     # SUV compacto clásico
etiquetas[('CHEVROLET', 'SPORTVAN')]     = 'sedan_familiar'   # Van de pasajeros
etiquetas[('CHEVROLET', 'LUMINA MINIVAN')]= 'sedan_familiar'  # Minivan familiar
etiquetas[('CHEVROLET', 'CHEVY VAN')]    = 'sedan_familiar'   # Van carga/pasajeros
etiquetas[('CHEVROLET', 'C/K 1500 SERIES')]= 'aventura_pickup' # Pickup clásico 4WD
etiquetas[('CHEVROLET', 'C/K 2500 SERIES')]= 'aventura_pickup' # Pickup heavy duty
etiquetas[('CHEVROLET', 'TAHOE LIMITED/Z71')]= 'aventura_pickup' # Tahoe Z71 = off-road
etiquetas[('CHEVROLET', 'METRO')]        = 'compacto_urbano'  # Micro urbano, el más pequeño
etiquetas[('CHEVROLET', 'LUMINA')]       = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('CHEVROLET', 'PRIZM')]        = 'compacto_urbano'  # Corolla rebadgeado
etiquetas[('CHEVROLET', 'AVEO')]         = 'compacto_urbano'  # Subcompacto urbano
etiquetas[('CHEVROLET', 'SPARK')]        = 'compacto_urbano'  # Citycar básico
etiquetas[('CHEVROLET', 'CAVALIER')]     = 'compacto_urbano'  # Coupe compacto accesible
etiquetas[('CHEVROLET', 'COBALT')]       = 'compacto_urbano'  # Coupe compacto
etiquetas[('CHEVROLET', 'SONIC')]        = 'compacto_urbano'  # Subcompacto moderno
etiquetas[('CHEVROLET', 'MALIBU CLASSIC')]= 'sedan_familiar'  # Sedán familiar
etiquetas[('CHEVROLET', 'S-10')]         = 'aventura_pickup'  # Pickup compacto clásico
etiquetas[('CHEVROLET', 'CLASSIC')]      = 'sedan_familiar'   # Malibu Classic
etiquetas[('CHEVROLET', 'TRACKER')]      = 'suv_familiar'     # SUV compacto 4WD
etiquetas[('CHEVROLET', 'CRUZE LIMITED')]= 'compacto_urbano'  # Compacto accesible
etiquetas[('CHEVROLET', 'CRUZE')]        = 'compacto_urbano'  # Compacto moderno popular
etiquetas[('CHEVROLET', 'HHR')]          = 'compacto_urbano'  # Wagon retro compacto
etiquetas[('CHEVROLET', 'MALIBU MAXX')]  = 'sedan_familiar'   # Hatchback familiar
etiquetas[('CHEVROLET', 'CITY EXPRESS')] = 'sedan_familiar'   # Van de carga comercial
etiquetas[('CHEVROLET', 'TRAX')]         = 'suv_familiar'     # SUV compacto urbano
etiquetas[('CHEVROLET', 'ASTRO CARGO')]  = 'sedan_familiar'   # Van de carga
etiquetas[('CHEVROLET', 'MONTE CARLO')]  = 'deportivo'        # Coupe personal luxury
etiquetas[('CHEVROLET', 'BLAZER')]       = 'suv_familiar'     # SUV compacto RWD
etiquetas[('CHEVROLET', 'MALIBU LIMITED')]= 'sedan_familiar'  # Sedán familiar
etiquetas[('CHEVROLET', 'UPLANDER')]     = 'sedan_familiar'   # Minivan familiar
etiquetas[('CHEVROLET', 'MALIBU HYBRID')]= 'sedan_familiar'   # Sedán híbrido familiar
etiquetas[('CHEVROLET', 'ASTRO')]        = 'sedan_familiar'   # Van de pasajeros
etiquetas[('CHEVROLET', 'MALIBU')]       = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('CHEVROLET', 'SPARK EV')]     = 'compacto_urbano'  # Eléctrico urbano
etiquetas[('CHEVROLET', 'CAPTIVA SPORT')]= 'suv_familiar'     # SUV mediano familiar
etiquetas[('CHEVROLET', 'VENTURE')]      = 'sedan_familiar'   # Minivan familiar
etiquetas[('CHEVROLET', 'SILVERADO 1500 CLASSIC')]= 'aventura_pickup' # Pickup clásico
etiquetas[('CHEVROLET', 'EQUINOX')]      = 'suv_familiar'     # SUV compacto popular
etiquetas[('CHEVROLET', 'COLORADO')]     = 'aventura_pickup'  # Pickup mediano trabajo/aventura
etiquetas[('CHEVROLET', 'IMPALA LIMITED')]= 'sedan_familiar'  # Sedán grande familiar
etiquetas[('CHEVROLET', 'TRAILBLAZER EXT')]= 'aventura_pickup' # SUV grande 4WD
etiquetas[('CHEVROLET', 'EXPRESS CARGO')]= 'sedan_familiar'   # Van de carga comercial
etiquetas[('CHEVROLET', 'TRAILBLAZER')] = 'aventura_pickup'   # SUV mediano 4WD
etiquetas[('CHEVROLET', 'IMPALA')]       = 'sedan_familiar'   # Sedán grande familiar
etiquetas[('CHEVROLET', 'EXPRESS')]      = 'sedan_familiar'   # Van de pasajeros
etiquetas[('CHEVROLET', 'TRAVERSE')]     = 'suv_familiar'     # SUV grande 3 filas familiar
etiquetas[('CHEVROLET', 'BOLT EV')]      = 'compacto_urbano'  # Eléctrico compacto urbano
etiquetas[('CHEVROLET', 'SILVERADO 1500')]= 'aventura_pickup' # Pickup grande 4WD
etiquetas[('CHEVROLET', 'CAMARO')]       = 'deportivo'        # Muscle car icónico
etiquetas[('CHEVROLET', 'SSR')]          = 'deportivo'        # Pickup retro deportivo
etiquetas[('CHEVROLET', 'BLACK DIAMOND AVALANCHE')]= 'aventura_pickup' # Pickup 4WD
etiquetas[('CHEVROLET', 'AVALANCHE')]    = 'aventura_pickup'  # Pickup 4WD grande
etiquetas[('CHEVROLET', 'SILVERADO 1500 HYBRID')]= 'aventura_pickup' # Pickup híbrido
etiquetas[('CHEVROLET', 'SS')]           = 'deportivo'        # Sedán performance australiano
etiquetas[('CHEVROLET', 'TAHOE HYBRID')] = 'aventura_pickup'  # SUV grande 4WD híbrido
etiquetas[('CHEVROLET', 'TAHOE')]        = 'aventura_pickup'  # SUV grande 4WD icónico
etiquetas[('CHEVROLET', 'CORVETTE STINGRAY')]= 'deportivo'    # Superdeportivo americano
etiquetas[('CHEVROLET', 'SUBURBAN')]     = 'aventura_pickup'  # SUV más grande del mercado
etiquetas[('CHEVROLET', 'CORVETTE')]     = 'deportivo'        # Deportivo americano puro

# ── CHRYSLER ──────────────────────────────────────────────────────
etiquetas[('CHRYSLER', 'LE BARON')]      = 'sedan_familiar'   # Convertible familiar accesible
etiquetas[('CHRYSLER', 'NEW YORKER')]    = 'sedan_familiar'   # Sedán grande familiar
etiquetas[('CHRYSLER', 'IMPERIAL')]      = 'lujo_sedan'       # Sedán lujo Chrysler
etiquetas[('CHRYSLER', 'TC')]            = 'deportivo'        # Convertible TC by Maserati
etiquetas[('CHRYSLER', 'GRAND VOYAGER')] = 'sedan_familiar'   # Minivan familiar grande
etiquetas[('CHRYSLER', 'CIRRUS')]        = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('CHRYSLER', 'LHS')]           = 'lujo_sedan'       # Sedán grande premium Chrysler
etiquetas[('CHRYSLER', 'PT CRUISER')]    = 'compacto_urbano'  # Wagon retro compacto
etiquetas[('CHRYSLER', 'VOYAGER')]       = 'sedan_familiar'   # Minivan familiar
etiquetas[('CHRYSLER', 'CONCORDE')]      = 'sedan_familiar'   # Sedán grande familiar
etiquetas[('CHRYSLER', 'SEBRING')]       = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('CHRYSLER', '200')]           = 'sedan_familiar'   # Sedán mediano moderno
etiquetas[('CHRYSLER', '300M')]          = 'lujo_sedan'       # Sedán grande premium
etiquetas[('CHRYSLER', 'PACIFICA')]      = 'sedan_familiar'   # Wagon grande familiar
etiquetas[('CHRYSLER', 'TOWN AND COUNTRY')]= 'sedan_familiar' # Minivan familiar premium
etiquetas[('CHRYSLER', 'ASPEN')]         = 'aventura_pickup'  # SUV grande 4WD
etiquetas[('CHRYSLER', 'CROSSFIRE')]     = 'deportivo'        # Roadster deportivo
etiquetas[('CHRYSLER', '300')]           = 'lujo_sedan'       # Sedán grande premium americano
etiquetas[('CHRYSLER', 'PROWLER')]       = 'deportivo'        # Roadster retro deportivo

# ── DODGE ─────────────────────────────────────────────────────────
etiquetas[('DODGE', 'COLT')]             = 'compacto_urbano'  # Subcompacto básico
etiquetas[('DODGE', 'MONACO')]           = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('DODGE', 'DYNASTY')]          = 'sedan_familiar'   # Sedán grande familiar
etiquetas[('DODGE', 'DAYTONA')]          = 'deportivo'        # Hatchback deportivo
etiquetas[('DODGE', 'SHADOW')]           = 'compacto_urbano'  # Hatchback compacto
etiquetas[('DODGE', 'RAMCHARGER')]       = 'aventura_pickup'  # SUV 4WD grande
etiquetas[('DODGE', 'RAM 50 PICKUP')]    = 'aventura_pickup'  # Pickup compacto
etiquetas[('DODGE', 'OMNI')]             = 'compacto_urbano'  # Hatchback básico
etiquetas[('DODGE', 'SPIRIT')]           = 'compacto_urbano'  # Sedán compacto
etiquetas[('DODGE', 'RAM 150')]          = 'aventura_pickup'  # Pickup grande
etiquetas[('DODGE', 'RAM 250')]          = 'aventura_pickup'  # Pickup heavy duty
etiquetas[('DODGE', 'RAM VAN')]          = 'sedan_familiar'   # Van de carga
etiquetas[('DODGE', 'STEALTH')]          = 'deportivo'        # Coupe deportivo turbo
etiquetas[('DODGE', 'RAM WAGON')]        = 'sedan_familiar'   # Van de pasajeros
etiquetas[('DODGE', 'NEON')]             = 'compacto_urbano'  # Sedán compacto accesible
etiquetas[('DODGE', 'CALIBER')]          = 'compacto_urbano'  # Wagon compacto
etiquetas[('DODGE', 'DART')]             = 'compacto_urbano'  # Sedán compacto moderno
etiquetas[('DODGE', 'CARAVAN')]          = 'sedan_familiar'   # Minivan familiar icónica
etiquetas[('DODGE', 'RAM CARGO')]        = 'sedan_familiar'   # Van de carga
etiquetas[('DODGE', 'STRATUS')]          = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('DODGE', 'AVENGER')]          = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('DODGE', 'INTREPID')]         = 'sedan_familiar'   # Sedán grande familiar
etiquetas[('DODGE', 'NITRO')]            = 'suv_familiar'     # SUV mediano 4WD
etiquetas[('DODGE', 'DAKOTA')]           = 'aventura_pickup'  # Pickup mediano 4WD
etiquetas[('DODGE', 'GRAND CARAVAN')]    = 'sedan_familiar'   # Minivan grande familiar
etiquetas[('DODGE', 'JOURNEY')]          = 'suv_familiar'     # SUV mediano familiar
etiquetas[('DODGE', 'RAM PICKUP 1500')]  = 'aventura_pickup'  # Pickup grande 4WD
etiquetas[('DODGE', 'MAGNUM')]           = 'sedan_familiar'   # Wagon grande RWD
etiquetas[('DODGE', 'CHARGER')]          = 'deportivo'        # Muscle car sedán
etiquetas[('DODGE', 'CHALLENGER')]       = 'deportivo'        # Muscle car coupe icónico
etiquetas[('DODGE', 'DURANGO')]          = 'aventura_pickup'  # SUV grande AWD
etiquetas[('DODGE', 'VIPER')]            = 'hiper_lujo'       # Superdeportivo americano $100k+
etiquetas[('DODGE', 'SRT VIPER')]        = 'hiper_lujo'       # SRT Viper — máximo rendimiento

# ── FERRARI ───────────────────────────────────────────────────────
for model in ['360','CALIFORNIA','CALIFORNIA T','F430','575M','456M','550',
              '458 ITALIA','SUPERAMERICA','FF','612 SCAGLIETTI',
              'F12 BERLINETTA','599','ENZO']:
    etiquetas[('FERRARI', model)] = 'hiper_lujo'

# ── FIAT ──────────────────────────────────────────────────────────
etiquetas[('FIAT', '500')]               = 'compacto_urbano'  # Citycar icónico
etiquetas[('FIAT', '500L')]              = 'compacto_urbano'  # Versión familiar del 500
etiquetas[('FIAT', '500X')]              = 'suv_familiar'     # Crossover compacto
etiquetas[('FIAT', '124 SPIDER')]        = 'deportivo'        # Roadster deportivo RWD

# ── FORD ──────────────────────────────────────────────────────────
etiquetas[('FORD', 'AEROSTAR')]          = 'sedan_familiar'   # Minivan familiar 90s
etiquetas[('FORD', 'ASPIRE')]            = 'compacto_urbano'  # Subcompacto básico
etiquetas[('FORD', 'BRONCO II')]         = 'suv_familiar'     # SUV compacto 4WD
etiquetas[('FORD', 'FESTIVA')]           = 'compacto_urbano'  # Micro urbano
etiquetas[('FORD', 'LTD CROWN VICTORIA')]= 'sedan_familiar'   # Wagon grande familiar
etiquetas[('FORD', 'TEMPO')]             = 'compacto_urbano'  # Sedán compacto básico
etiquetas[('FORD', 'PROBE')]             = 'deportivo'        # Hatchback deportivo
etiquetas[('FORD', 'CONTOUR')]           = 'compacto_urbano'  # Sedán compacto europeo
etiquetas[('FORD', 'E-250')]             = 'sedan_familiar'   # Van de carga
etiquetas[('FORD', 'E-150')]             = 'sedan_familiar'   # Van de pasajeros
etiquetas[('FORD', 'BRONCO')]            = 'aventura_pickup'  # SUV 4WD icónico
etiquetas[('FORD', 'CONTOUR SVT')]       = 'deportivo'        # Sedán compacto performance
etiquetas[('FORD', 'F-250')]             = 'aventura_pickup'  # Pickup heavy duty 4WD
etiquetas[('FORD', 'MUSTANG SVT COBRA')] = 'deportivo'        # Mustang máximo rendimiento
etiquetas[('FORD', 'F-150 SVT LIGHTNING')]= 'deportivo'       # F-150 performance especial
etiquetas[('FORD', 'ESCORT')]            = 'compacto_urbano'  # Compacto accesible
etiquetas[('FORD', 'FIESTA')]            = 'compacto_urbano'  # Subcompacto urbano
etiquetas[('FORD', 'WINDSTAR CARGO')]    = 'sedan_familiar'   # Minivan carga
etiquetas[('FORD', 'RANGER')]            = 'aventura_pickup'  # Pickup compacto clásico
etiquetas[('FORD', 'FOCUS')]             = 'compacto_urbano'  # Compacto popular mundial
etiquetas[('FORD', 'F-150 HERITAGE')]    = 'aventura_pickup'  # Pickup clásico 4WD
etiquetas[('FORD', 'EXPLORER SPORT')]    = 'suv_familiar'     # SUV mediano 4WD
etiquetas[('FORD', 'FOCUS ST')]          = 'deportivo'        # Focus performance hot hatch
etiquetas[('FORD', 'TRANSIT CONNECT')]   = 'sedan_familiar'   # Van comercial compacta
etiquetas[('FORD', 'FIVE HUNDRED')]      = 'sedan_familiar'   # Sedán grande familiar
etiquetas[('FORD', 'C-MAX HYBRID')]      = 'sedan_familiar'   # Híbrido familiar wagon
etiquetas[('FORD', 'FREESTAR')]          = 'sedan_familiar'   # Minivan familiar
etiquetas[('FORD', 'ESCAPE')]            = 'suv_familiar'     # SUV compacto popular
etiquetas[('FORD', 'FREESTYLE')]         = 'sedan_familiar'   # Wagon grande AWD
etiquetas[('FORD', 'WINDSTAR')]          = 'sedan_familiar'   # Minivan familiar
etiquetas[('FORD', 'FUSION')]            = 'sedan_familiar'   # Sedán mediano popular
etiquetas[('FORD', 'FUSION HYBRID')]     = 'sedan_familiar'   # Sedán híbrido familiar
etiquetas[('FORD', 'CROWN VICTORIA')]    = 'sedan_familiar'   # Sedán grande americano
etiquetas[('FORD', 'E-SERIES VAN')]      = 'sedan_familiar'   # Van grande carga
etiquetas[('FORD', 'EXPLORER SPORT TRAC')]= 'aventura_pickup' # Pickup/SUV deportivo
etiquetas[('FORD', 'TAURUS X')]          = 'suv_familiar'     # SUV grande familiar
etiquetas[('FORD', 'ESCAPE HYBRID')]     = 'suv_familiar'     # SUV compacto híbrido
etiquetas[('FORD', 'MUSTANG')]           = 'deportivo'        # Muscle car icónico
etiquetas[('FORD', 'E-SERIES WAGON')]    = 'sedan_familiar'   # Van pasajeros
etiquetas[('FORD', 'TAURUS')]            = 'sedan_familiar'   # Sedán grande familiar
etiquetas[('FORD', 'EDGE')]              = 'suv_familiar'     # SUV mediano popular
etiquetas[('FORD', 'FOCUS RS')]          = 'deportivo'        # Hot hatch máximo rendimiento
etiquetas[('FORD', 'FLEX')]              = 'sedan_familiar'   # Wagon grande familiar
etiquetas[('FORD', 'TRANSIT WAGON')]     = 'sedan_familiar'   # Van pasajeros grande
etiquetas[('FORD', 'EXPLORER')]          = 'suv_familiar'     # SUV grande familiar referente
etiquetas[('FORD', 'THUNDERBIRD')]       = 'deportivo'        # Convertible retro deportivo
etiquetas[('FORD', 'F-150')]             = 'aventura_pickup'  # Pickup más vendido de EEUU
etiquetas[('FORD', 'SHELBY GT500')]      = 'deportivo'        # Mustang máximo rendimiento
etiquetas[('FORD', 'SHELBY GT350')]      = 'deportivo'        # Mustang performance track
etiquetas[('FORD', 'EXPEDITION')]        = 'aventura_pickup'  # SUV grande 4WD
etiquetas[('FORD', 'GT')]                = 'hiper_lujo'       # Superdeportivo $150k

# ── GENESIS ───────────────────────────────────────────────────────
etiquetas[('GENESIS', 'G80')]            = 'lujo_sedan'       # Sedán premium coreano

# ── GMC ───────────────────────────────────────────────────────────
etiquetas[('GMC', 'RALLY WAGON')]        = 'sedan_familiar'   # Van pasajeros
etiquetas[('GMC', 'S-15')]               = 'aventura_pickup'  # Pickup compacto
etiquetas[('GMC', 'S-15 JIMMY')]         = 'suv_familiar'     # SUV compacto 4WD
etiquetas[('GMC', 'VANDURA')]            = 'sedan_familiar'   # Van de carga
etiquetas[('GMC', 'SUBURBAN')]           = 'aventura_pickup'  # SUV grande icónico
etiquetas[('GMC', 'YUKON DENALI')]       = 'lujo_suv'         # SUV grande lujo premium
etiquetas[('GMC', 'SIERRA CLASSIC 1500')]= 'aventura_pickup'  # Pickup grande 4WD
etiquetas[('GMC', 'SYCLONE')]            = 'deportivo'        # Pickup deportivo turbo AWD
etiquetas[('GMC', 'TYPHOON')]            = 'deportivo'        # SUV deportivo turbo AWD
etiquetas[('GMC', 'JIMMY')]              = 'suv_familiar'     # SUV mediano 4WD
etiquetas[('GMC', 'SONOMA')]             = 'aventura_pickup'  # Pickup compacto
etiquetas[('GMC', 'SAFARI CARGO')]       = 'sedan_familiar'   # Van carga AWD
etiquetas[('GMC', 'SAFARI')]             = 'sedan_familiar'   # Van pasajeros AWD
etiquetas[('GMC', 'SIERRA 1500 CLASSIC')]= 'aventura_pickup'  # Pickup grande 4WD
etiquetas[('GMC', 'CANYON')]             = 'aventura_pickup'  # Pickup mediano
etiquetas[('GMC', 'TERRAIN')]            = 'suv_familiar'     # SUV compacto familiar
etiquetas[('GMC', 'SAVANA CARGO')]       = 'sedan_familiar'   # Van de carga
etiquetas[('GMC', 'ENVOY XUV')]          = 'aventura_pickup'  # SUV grande 4WD
etiquetas[('GMC', 'ENVOY')]              = 'suv_familiar'     # SUV mediano 4WD
etiquetas[('GMC', 'SIERRA 1500HD')]      = 'aventura_pickup'  # Pickup heavy duty 4WD
etiquetas[('GMC', 'ENVOY XL')]           = 'aventura_pickup'  # SUV grande 4WD
etiquetas[('GMC', 'SAVANA')]             = 'sedan_familiar'   # Van pasajeros
etiquetas[('GMC', 'SIERRA C3')]          = 'aventura_pickup'  # Pickup grande AWD
etiquetas[('GMC', 'ACADIA')]             = 'suv_familiar'     # SUV grande 3 filas familiar
etiquetas[('GMC', 'SIERRA 1500')]        = 'aventura_pickup'  # Pickup grande 4WD
etiquetas[('GMC', 'ACADIA LIMITED')]     = 'suv_familiar'     # SUV grande familiar
etiquetas[('GMC', 'SIERRA 1500 HYBRID')] = 'aventura_pickup'  # Pickup híbrido
etiquetas[('GMC', 'YUKON HYBRID')]       = 'lujo_suv'         # SUV grande lujo híbrido
etiquetas[('GMC', 'YUKON')]              = 'aventura_pickup'  # SUV grande 4WD
etiquetas[('GMC', 'YUKON XL')]           = 'aventura_pickup'  # SUV grande extendido

# ── HONDA ─────────────────────────────────────────────────────────
etiquetas[('HONDA', 'CIVIC CRX')]        = 'deportivo'        # Hatchback deportivo icónico 80s
etiquetas[('HONDA', 'CIVIC DEL SOL')]    = 'deportivo'        # Targa deportivo
etiquetas[('HONDA', 'PRELUDE')]          = 'deportivo'        # Coupe deportivo
etiquetas[('HONDA', 'FIT')]              = 'compacto_urbano'  # Subcompacto versátil urbano
etiquetas[('HONDA', 'INSIGHT')]          = 'compacto_urbano'  # Híbrido compacto urbano
etiquetas[('HONDA', 'PASSPORT')]         = 'suv_familiar'     # SUV mediano 4WD
etiquetas[('HONDA', 'CR-Z')]             = 'deportivo'        # Híbrido deportivo coupe
etiquetas[('HONDA', 'HR-V')]             = 'suv_familiar'     # SUV compacto urbano
etiquetas[('HONDA', 'CIVIC')]            = 'compacto_urbano'  # Compacto icónico urbano
etiquetas[('HONDA', 'ELEMENT')]          = 'suv_familiar'     # SUV compacto versátil
etiquetas[('HONDA', 'ACCORD')]           = 'sedan_familiar'   # Sedán mediano referente
etiquetas[('HONDA', 'CR-V')]             = 'suv_familiar'     # SUV compacto popular
etiquetas[('HONDA', 'ACCORD HYBRID')]    = 'sedan_familiar'   # Sedán híbrido familiar
etiquetas[('HONDA', 'CROSSTOUR')]        = 'suv_familiar'     # Crossover hatchback
etiquetas[('HONDA', 'ACCORD CROSSTOUR')] = 'suv_familiar'     # Crossover Accord
etiquetas[('HONDA', 'RIDGELINE')]        = 'aventura_pickup'  # Pickup familiar Honda
etiquetas[('HONDA', 'S2000')]            = 'deportivo'        # Roadster deportivo puro RWD
etiquetas[('HONDA', 'ODYSSEY')]          = 'sedan_familiar'   # Minivan familiar referente
etiquetas[('HONDA', 'PILOT')]            = 'suv_familiar'     # SUV grande familiar
etiquetas[('HONDA', 'ACCORD PLUG-IN HYBRID')]= 'sedan_familiar' # Sedán PHEV familiar

# ── HUMMER ────────────────────────────────────────────────────────
etiquetas[('HUMMER', 'H3T')]             = 'aventura_pickup'  # Pickup 4WD extremo
etiquetas[('HUMMER', 'H3')]              = 'aventura_pickup'  # SUV 4WD extremo

# ── HYUNDAI ───────────────────────────────────────────────────────
etiquetas[('HYUNDAI', 'SCOUPE')]         = 'compacto_urbano'  # Coupe compacto básico
etiquetas[('HYUNDAI', 'EXCEL')]          = 'compacto_urbano'  # Subcompacto básico
etiquetas[('HYUNDAI', 'ACCENT')]         = 'compacto_urbano'  # Subcompacto urbano
etiquetas[('HYUNDAI', 'ELANTRA TOURING')]= 'compacto_urbano'  # Hatchback compacto
etiquetas[('HYUNDAI', 'ELANTRA GT')]     = 'compacto_urbano'  # Hatchback compacto premium
etiquetas[('HYUNDAI', 'ELANTRA COUPE')]  = 'compacto_urbano'  # Coupe compacto
etiquetas[('HYUNDAI', 'TIBURON')]        = 'deportivo'        # Coupe deportivo
etiquetas[('HYUNDAI', 'ELANTRA')]        = 'compacto_urbano'  # Compacto popular
etiquetas[('HYUNDAI', 'VELOSTER')]       = 'deportivo'        # Hatchback deportivo 3 puertas
etiquetas[('HYUNDAI', 'XG300')]          = 'lujo_sedan'       # Sedán grande premium
etiquetas[('HYUNDAI', 'XG350')]          = 'lujo_sedan'       # Sedán grande premium
etiquetas[('HYUNDAI', 'SONATA')]         = 'sedan_familiar'   # Sedán mediano popular
etiquetas[('HYUNDAI', 'TUCSON')]         = 'suv_familiar'     # SUV compacto popular
etiquetas[('HYUNDAI', 'ENTOURAGE')]      = 'sedan_familiar'   # Minivan familiar
etiquetas[('HYUNDAI', 'SONATA HYBRID')]  = 'sedan_familiar'   # Sedán híbrido familiar
etiquetas[('HYUNDAI', 'SANTA FE SPORT')] = 'suv_familiar'     # SUV mediano familiar
etiquetas[('HYUNDAI', 'GENESIS COUPE')]  = 'deportivo'        # Coupe deportivo RWD
etiquetas[('HYUNDAI', 'VERACRUZ')]       = 'suv_familiar'     # SUV grande familiar
etiquetas[('HYUNDAI', 'SANTA FE')]       = 'suv_familiar'     # SUV grande familiar
etiquetas[('HYUNDAI', 'AZERA')]          = 'lujo_sedan'       # Sedán grande premium
etiquetas[('HYUNDAI', 'GENESIS')]        = 'lujo_sedan'       # Sedán grande premium RWD
etiquetas[('HYUNDAI', 'EQUUS')]          = 'lujo_sedan'       # Flagship sedán premium

# ── INFINITI ──────────────────────────────────────────────────────
etiquetas[('INFINITI', 'M30')]           = 'lujo_sedan'       # Coupe/sedán premium 90s
etiquetas[('INFINITI', 'J30')]           = 'lujo_sedan'       # Sedán premium RWD
etiquetas[('INFINITI', 'I30')]           = 'lujo_sedan'       # Sedán premium FWD
etiquetas[('INFINITI', 'G20')]           = 'lujo_sedan'       # Sedán compacto premium
etiquetas[('INFINITI', 'I35')]           = 'lujo_sedan'       # Sedán mediano premium
etiquetas[('INFINITI', 'G35')]           = 'lujo_sedan'       # Sedán/coupe premium RWD
etiquetas[('INFINITI', 'Q40')]           = 'lujo_sedan'       # Sedán compacto premium
etiquetas[('INFINITI', 'QX4')]           = 'lujo_suv'         # SUV mediano premium 4WD
etiquetas[('INFINITI', 'EX35')]          = 'lujo_suv'         # SUV compacto premium
etiquetas[('INFINITI', 'QX50')]          = 'lujo_suv'         # SUV compacto premium
etiquetas[('INFINITI', 'G37')]           = 'deportivo'        # Coupe RWD performance
etiquetas[('INFINITI', 'EX')]            = 'lujo_suv'         # SUV compacto premium
etiquetas[('INFINITI', 'G37 SEDAN')]     = 'lujo_sedan'       # Sedán performance premium
etiquetas[('INFINITI', 'G SEDAN')]       = 'lujo_sedan'       # Sedán mediano premium
etiquetas[('INFINITI', 'G37 COUPE')]     = 'deportivo'        # Coupe RWD performance
etiquetas[('INFINITI', 'FX35')]          = 'lujo_suv'         # SUV mediano premium AWD
etiquetas[('INFINITI', 'JX')]            = 'lujo_suv'         # SUV grande 3 filas premium
etiquetas[('INFINITI', 'Q50')]           = 'lujo_sedan'       # Sedán mediano premium
etiquetas[('INFINITI', 'G COUPE')]       = 'deportivo'        # Coupe premium performance
etiquetas[('INFINITI', 'Q60 COUPE')]     = 'deportivo'        # Coupe premium RWD
etiquetas[('INFINITI', 'QX60')]          = 'lujo_suv'         # SUV grande 3 filas premium
etiquetas[('INFINITI', 'M35')]           = 'lujo_sedan'       # Sedán ejecutivo premium
etiquetas[('INFINITI', 'QX70')]          = 'lujo_suv'         # SUV mediano premium
etiquetas[('INFINITI', 'M37')]           = 'lujo_sedan'       # Sedán ejecutivo AWD
etiquetas[('INFINITI', 'G37 CONVERTIBLE')]= 'deportivo'       # Convertible premium RWD
etiquetas[('INFINITI', 'FX45')]          = 'lujo_suv'         # SUV mediano premium
etiquetas[('INFINITI', 'FX')]            = 'lujo_suv'         # SUV mediano premium
etiquetas[('INFINITI', 'G CONVERTIBLE')] = 'deportivo'        # Convertible premium
etiquetas[('INFINITI', 'M45')]           = 'lujo_sedan'       # Sedán grande V8 premium
etiquetas[('INFINITI', 'Q60 CONVERTIBLE')]= 'deportivo'       # Convertible premium
etiquetas[('INFINITI', 'M')]             = 'lujo_sedan'       # Sedán ejecutivo
etiquetas[('INFINITI', 'Q45')]           = 'lujo_sedan'       # Flagship sedán premium
etiquetas[('INFINITI', 'Q70')]           = 'lujo_sedan'       # Sedán ejecutivo premium
etiquetas[('INFINITI', 'QX56')]          = 'lujo_suv'         # SUV grande premium 4WD
etiquetas[('INFINITI', 'FX50')]          = 'lujo_suv'         # SUV mediano premium V8
etiquetas[('INFINITI', 'M56')]           = 'lujo_sedan'       # Sedán V8 premium
etiquetas[('INFINITI', 'QX')]            = 'lujo_suv'         # SUV grande premium 4WD
etiquetas[('INFINITI', 'QX80')]          = 'lujo_suv'         # SUV grande flagship

# ── KIA ───────────────────────────────────────────────────────────
etiquetas[('KIA', 'SEPHIA')]             = 'compacto_urbano'  # Sedán compacto básico
etiquetas[('KIA', 'SPECTRA')]            = 'compacto_urbano'  # Sedán compacto accesible
etiquetas[('KIA', 'RIO')]                = 'compacto_urbano'  # Subcompacto urbano
etiquetas[('KIA', 'SOUL')]               = 'compacto_urbano'  # Wagon compacto urbano
etiquetas[('KIA', 'RONDO')]              = 'sedan_familiar'   # Wagon compacto familiar
etiquetas[('KIA', 'FORTE')]              = 'compacto_urbano'  # Compacto moderno
etiquetas[('KIA', 'AMANTI')]             = 'lujo_sedan'       # Sedán grande premium Kia
etiquetas[('KIA', 'SPORTAGE')]           = 'suv_familiar'     # SUV compacto popular
etiquetas[('KIA', 'OPTIMA')]             = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('KIA', 'OPTIMA HYBRID')]      = 'sedan_familiar'   # Sedán híbrido familiar
etiquetas[('KIA', 'BORREGO')]            = 'suv_familiar'     # SUV grande 4WD
etiquetas[('KIA', 'SEDONA')]             = 'sedan_familiar'   # Minivan familiar
etiquetas[('KIA', 'SORENTO')]            = 'suv_familiar'     # SUV mediano familiar
etiquetas[('KIA', 'CADENZA')]            = 'lujo_sedan'       # Sedán grande premium
etiquetas[('KIA', 'K900')]               = 'lujo_sedan'       # Flagship sedán premium RWD

# ── LAMBORGHINI ───────────────────────────────────────────────────
for model in ['GALLARDO','HURACAN','DIABLO','MURCIELAGO','AVENTADOR','REVENTON']:
    etiquetas[('LAMBORGHINI', model)] = 'hiper_lujo'

# ── LAND ROVER ────────────────────────────────────────────────────
etiquetas[('LAND ROVER', 'FREELANDER')]          = 'lujo_suv'      # SUV compacto premium
etiquetas[('LAND ROVER', 'DISCOVERY SERIES II')] = 'aventura_pickup' # SUV 4WD off-road real
etiquetas[('LAND ROVER', 'DEFENDER')]            = 'aventura_pickup' # SUV 4WD off-road icónico
etiquetas[('LAND ROVER', 'DISCOVERY')]           = 'aventura_pickup' # SUV 4WD aventura
etiquetas[('LAND ROVER', 'LR2')]                 = 'lujo_suv'      # SUV compacto premium
etiquetas[('LAND ROVER', 'DISCOVERY SPORT')]     = 'lujo_suv'      # SUV compacto premium
etiquetas[('LAND ROVER', 'LR3')]                 = 'lujo_suv'      # SUV mediano premium 4WD
etiquetas[('LAND ROVER', 'RANGE ROVER EVOQUE')]  = 'lujo_suv'      # SUV compacto lujo
etiquetas[('LAND ROVER', 'LR4')]                 = 'lujo_suv'      # SUV mediano premium 4WD
etiquetas[('LAND ROVER', 'RANGE ROVER SPORT')]   = 'lujo_suv'      # SUV mediano lujo 4WD
etiquetas[('LAND ROVER', 'RANGE ROVER')]         = 'hiper_lujo'    # Flagship $118k+ lujo extremo

# ── LEXUS ─────────────────────────────────────────────────────────
etiquetas[('LEXUS', 'ES 250')]           = 'lujo_sedan'       # Entry sedán Lexus
etiquetas[('LEXUS', 'SC 300')]           = 'deportivo'        # Coupe premium RWD
etiquetas[('LEXUS', 'GS 400')]           = 'lujo_sedan'       # Sedán ejecutivo V8
etiquetas[('LEXUS', 'SC 400')]           = 'deportivo'        # Coupe premium V8
etiquetas[('LEXUS', 'LX 450')]           = 'lujo_suv'         # SUV grande lujo 4WD
etiquetas[('LEXUS', 'LS 400')]           = 'lujo_sedan'       # Flagship sedán lujo
etiquetas[('LEXUS', 'CT 200H')]          = 'lujo_sedan'       # Hatchback híbrido premium
etiquetas[('LEXUS', 'ES 300')]           = 'lujo_sedan'       # Sedán mediano premium
etiquetas[('LEXUS', 'ES 330')]           = 'lujo_sedan'       # Sedán mediano premium
etiquetas[('LEXUS', 'IS 300')]           = 'lujo_sedan'       # Sedán compacto premium RWD
etiquetas[('LEXUS', 'RX 300')]           = 'lujo_suv'         # SUV mediano premium pionero
etiquetas[('LEXUS', 'RX 330')]           = 'lujo_suv'         # SUV mediano premium
etiquetas[('LEXUS', 'NX 200T')]          = 'lujo_suv'         # SUV compacto premium
etiquetas[('LEXUS', 'HS 250H')]          = 'lujo_sedan'       # Sedán híbrido premium
etiquetas[('LEXUS', 'IS 200T')]          = 'lujo_sedan'       # Sedán compacto premium
etiquetas[('LEXUS', 'IS 250')]           = 'lujo_sedan'       # Sedán compacto premium RWD
etiquetas[('LEXUS', 'ES 350')]           = 'lujo_sedan'       # Sedán mediano premium
etiquetas[('LEXUS', 'RC 200T')]          = 'deportivo'        # Coupe premium RWD
etiquetas[('LEXUS', 'NX 300H')]          = 'lujo_suv'         # SUV compacto híbrido premium
etiquetas[('LEXUS', 'ES 300H')]          = 'lujo_sedan'       # Sedán híbrido premium
etiquetas[('LEXUS', 'IS 350')]           = 'lujo_sedan'       # Sedán compacto premium AWD
etiquetas[('LEXUS', 'GS 300')]           = 'lujo_sedan'       # Sedán ejecutivo premium
etiquetas[('LEXUS', 'RC 300')]           = 'deportivo'        # Coupe premium AWD
etiquetas[('LEXUS', 'IS 250 C')]         = 'deportivo'        # Convertible premium RWD
etiquetas[('LEXUS', 'RX 400H')]          = 'lujo_suv'         # SUV mediano híbrido premium
etiquetas[('LEXUS', 'RC 350')]           = 'deportivo'        # Coupe premium performance
etiquetas[('LEXUS', 'RX 350')]           = 'lujo_suv'         # SUV mediano premium referente
etiquetas[('LEXUS', 'GX 470')]           = 'lujo_suv'         # SUV mediano premium 4WD
etiquetas[('LEXUS', 'IS 350 C')]         = 'deportivo'        # Convertible premium performance
etiquetas[('LEXUS', 'GS 200T')]          = 'lujo_sedan'       # Sedán ejecutivo premium
etiquetas[('LEXUS', 'GS 430')]           = 'lujo_sedan'       # Sedán ejecutivo V8
etiquetas[('LEXUS', 'GS 350')]           = 'lujo_sedan'       # Sedán ejecutivo premium
etiquetas[('LEXUS', 'RX 450H')]          = 'lujo_suv'         # SUV mediano híbrido premium
etiquetas[('LEXUS', 'GS 460')]           = 'lujo_sedan'       # Sedán ejecutivo V8
etiquetas[('LEXUS', 'LS 430')]           = 'lujo_sedan'       # Flagship sedán lujo
etiquetas[('LEXUS', 'GX 460')]           = 'lujo_suv'         # SUV mediano premium 4WD
etiquetas[('LEXUS', 'GS 450H')]          = 'lujo_sedan'       # Sedán ejecutivo híbrido
etiquetas[('LEXUS', 'IS F')]             = 'deportivo'        # Sedán compacto performance
etiquetas[('LEXUS', 'RC F')]             = 'deportivo'        # Coupe performance V8
etiquetas[('LEXUS', 'LX 470')]           = 'lujo_suv'         # SUV grande premium 4WD
etiquetas[('LEXUS', 'SC 430')]           = 'deportivo'        # Convertible premium
etiquetas[('LEXUS', 'LS 460')]           = 'lujo_sedan'       # Flagship sedán lujo AWD
etiquetas[('LEXUS', 'GS F')]             = 'deportivo'        # Sedán performance V8
etiquetas[('LEXUS', 'LX 570')]           = 'lujo_suv'         # SUV grande premium 4WD
etiquetas[('LEXUS', 'LS 600H L')]        = 'hiper_lujo'       # Flagship híbrido $120k+
etiquetas[('LEXUS', 'LFA')]              = 'hiper_lujo'       # Superdeportivo $375k

# ── LINCOLN ───────────────────────────────────────────────────────
etiquetas[('LINCOLN', 'MARK VII')]       = 'lujo_sedan'       # Coupe lujo americano
etiquetas[('LINCOLN', 'MARK VIII')]      = 'lujo_sedan'       # Coupe lujo americano
etiquetas[('LINCOLN', 'ZEPHYR')]         = 'lujo_sedan'       # Sedán mediano premium
etiquetas[('LINCOLN', 'MKZ HYBRID')]     = 'lujo_sedan'       # Sedán híbrido premium
etiquetas[('LINCOLN', 'LS')]             = 'lujo_sedan'       # Sedán mediano premium RWD
etiquetas[('LINCOLN', 'MARK LT')]        = 'aventura_pickup'  # Pickup premium Lincoln
etiquetas[('LINCOLN', 'MKC')]            = 'lujo_suv'         # SUV compacto premium
etiquetas[('LINCOLN', 'MKZ')]            = 'lujo_sedan'       # Sedán mediano premium
etiquetas[('LINCOLN', 'MKS')]            = 'lujo_sedan'       # Sedán grande premium
etiquetas[('LINCOLN', 'AVIATOR')]        = 'lujo_suv'         # SUV mediano premium
etiquetas[('LINCOLN', 'MKT')]            = 'lujo_suv'         # Wagon grande premium
etiquetas[('LINCOLN', 'MKX')]            = 'lujo_suv'         # SUV mediano premium
etiquetas[('LINCOLN', 'CONTINENTAL')]    = 'lujo_sedan'       # Flagship sedán lujo
etiquetas[('LINCOLN', 'TOWN CAR')]       = 'lujo_sedan'       # Sedán grande lujo icónico
etiquetas[('LINCOLN', 'BLACKWOOD')]      = 'aventura_pickup'  # Pickup lujo premium
etiquetas[('LINCOLN', 'NAVIGATOR')]      = 'lujo_suv'         # SUV grande premium

# ── LOTUS ─────────────────────────────────────────────────────────
# Lotus es puro deportivo — todos son autos de pista accesibles o semicoleccionistas
etiquetas[('LOTUS', 'ELISE')]            = 'deportivo'        # Roadster puro pista $52k
etiquetas[('LOTUS', 'EXIGE')]            = 'deportivo'        # Coupe pista $70k
etiquetas[('LOTUS', 'EVORA')]            = 'deportivo'        # GT coupe premium
etiquetas[('LOTUS', 'ESPRIT')]           = 'deportivo'        # Coupe deportivo clásico
etiquetas[('LOTUS', 'EVORA 400')]        = 'deportivo'        # Coupe performance $92k

# ── MASERATI ──────────────────────────────────────────────────────
etiquetas[('MASERATI', 'GHIBLI')]        = 'lujo_sedan'       # Sedán entry Maserati
etiquetas[('MASERATI', 'LEVANTE')]       = 'lujo_suv'         # SUV grande Maserati
etiquetas[('MASERATI', 'COUPE')]         = 'deportivo'        # Coupe deportivo $84k
etiquetas[('MASERATI', 'SPYDER')]        = 'deportivo'        # Convertible deportivo $88k
etiquetas[('MASERATI', 'GRANSPORT')]     = 'hiper_lujo'       # Coupe performance $100k+
etiquetas[('MASERATI', 'QUATTROPORTE')] = 'hiper_lujo'        # Sedán flagship $119k+
etiquetas[('MASERATI', 'GRANTURISMO')]   = 'hiper_lujo'       # Coupe gran turismo $146k
etiquetas[('MASERATI', 'GRANTURISMO CONVERTIBLE')]= 'hiper_lujo' # Convertible GT $156k

# ── MAYBACH ───────────────────────────────────────────────────────
for model in ['57', '62', 'LANDAULET']:
    etiquetas[('MAYBACH', model)] = 'hiper_lujo'              # Ultra lujo $400k+

# ── MAZDA ─────────────────────────────────────────────────────────
etiquetas[('MAZDA', '323')]              = 'compacto_urbano'  # Subcompacto básico
etiquetas[('MAZDA', '929')]              = 'lujo_sedan'       # Sedán grande premium RWD
etiquetas[('MAZDA', 'NAVAJO')]           = 'suv_familiar'     # SUV compacto 4WD
etiquetas[('MAZDA', 'MX-6')]             = 'deportivo'        # Coupe deportivo
etiquetas[('MAZDA', 'MX-3')]             = 'deportivo'        # Coupe compacto deportivo
etiquetas[('MAZDA', 'B-SERIES PICKUP')]  = 'aventura_pickup'  # Pickup compacto
etiquetas[('MAZDA', 'RX-7')]             = 'deportivo'        # Coupe rotativo icónico RWD
etiquetas[('MAZDA', '626')]              = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('MAZDA', 'PROTEGE')]          = 'compacto_urbano'  # Sedán compacto
etiquetas[('MAZDA', '2')]                = 'compacto_urbano'  # Subcompacto urbano
etiquetas[('MAZDA', 'PROTEGE5')]         = 'compacto_urbano'  # Wagon compacto
etiquetas[('MAZDA', 'B-SERIES')]         = 'aventura_pickup'  # Pickup compacto
etiquetas[('MAZDA', 'TRUCK')]            = 'aventura_pickup'  # Pickup compacto
etiquetas[('MAZDA', 'MAZDASPEED PROTEGE')]= 'deportivo'       # Compacto turbo performance
etiquetas[('MAZDA', 'B-SERIES TRUCK')]   = 'aventura_pickup'  # Pickup compacto
etiquetas[('MAZDA', 'MILLENIA')]         = 'lujo_sedan'       # Sedán mediano premium
etiquetas[('MAZDA', '5')]                = 'sedan_familiar'   # Minivan compacta familiar
etiquetas[('MAZDA', '3')]                = 'compacto_urbano'  # Compacto popular moderno
etiquetas[('MAZDA', 'CX-3')]             = 'suv_familiar'     # SUV compacto urbano
etiquetas[('MAZDA', 'MAZDASPEED 3')]     = 'deportivo'        # 3 turbo hot hatch
etiquetas[('MAZDA', 'TRIBUTE')]          = 'suv_familiar'     # SUV compacto familiar
etiquetas[('MAZDA', '6')]                = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('MAZDA', 'MPV')]              = 'sedan_familiar'   # Minivan familiar
etiquetas[('MAZDA', 'CX-5')]             = 'suv_familiar'     # SUV mediano popular
etiquetas[('MAZDA', 'MAZDASPEED MX-5 MIATA')]= 'deportivo'   # Miata turbo performance
etiquetas[('MAZDA', 'CX-7')]             = 'suv_familiar'     # SUV mediano familiar
etiquetas[('MAZDA', 'MX-5 MIATA')]       = 'deportivo'        # Roadster icónico más vendido mundo
etiquetas[('MAZDA', 'MAZDASPEED 6')]     = 'deportivo'        # 6 turbo performance
etiquetas[('MAZDA', 'TRIBUTE HYBRID')]   = 'suv_familiar'     # SUV compacto híbrido
etiquetas[('MAZDA', 'RX-8')]             = 'deportivo'        # Coupe rotativo 4 puertas RWD
etiquetas[('MAZDA', 'CX-9')]             = 'suv_familiar'     # SUV grande 3 filas familiar

# ── MCLAREN ───────────────────────────────────────────────────────
for model in ['570S', 'MP4-12C', '650S COUPE', '650S SPIDER']:
    etiquetas[('MCLAREN', model)] = 'hiper_lujo'              # Superdeportivos $185k-$280k

# ── MERCEDES-BENZ ─────────────────────────────────────────────────
etiquetas[('MERCEDES-BENZ', '190-CLASS')]   = 'lujo_sedan'    # Sedán compacto premium 90s
etiquetas[('MERCEDES-BENZ', '420-CLASS')]   = 'lujo_sedan'    # Sedán grande lujo
etiquetas[('MERCEDES-BENZ', '350-CLASS')]   = 'lujo_sedan'    # Sedán grande lujo
etiquetas[('MERCEDES-BENZ', '560-CLASS')]   = 'lujo_sedan'    # Coupe grande lujo
etiquetas[('MERCEDES-BENZ', '300-CLASS')]   = 'lujo_sedan'    # Sedán mediano premium
etiquetas[('MERCEDES-BENZ', '400-CLASS')]   = 'lujo_sedan'    # Sedán grande lujo
etiquetas[('MERCEDES-BENZ', '600-CLASS')]   = 'hiper_lujo'    # Mega flagship lujo
etiquetas[('MERCEDES-BENZ', '500-CLASS')]   = 'lujo_sedan'    # Sedán compacto lujo
etiquetas[('MERCEDES-BENZ', 'C36 AMG')]     = 'deportivo'     # AMG = performance
etiquetas[('MERCEDES-BENZ', 'C43 AMG')]     = 'deportivo'     # AMG performance
etiquetas[('MERCEDES-BENZ', 'ML55 AMG')]    = 'lujo_suv'      # SUV AMG performance
etiquetas[('MERCEDES-BENZ', 'E55 AMG')]     = 'deportivo'     # Sedán AMG performance
etiquetas[('MERCEDES-BENZ', 'METRIS')]      = 'sedan_familiar' # Van comercial
etiquetas[('MERCEDES-BENZ', 'CLA-CLASS')]   = 'lujo_sedan'    # Sedán compacto premium entry
etiquetas[('MERCEDES-BENZ', 'GLA-CLASS')]   = 'lujo_suv'      # SUV compacto premium
etiquetas[('MERCEDES-BENZ', 'GLK-CLASS')]   = 'lujo_suv'      # SUV compacto premium
etiquetas[('MERCEDES-BENZ', 'GLC-CLASS')]   = 'lujo_suv'      # SUV compacto premium moderno
etiquetas[('MERCEDES-BENZ', 'B-CLASS ELECTRIC DRIVE')]= 'lujo_sedan' # Hatchback eléctrico premium
etiquetas[('MERCEDES-BENZ', 'C-CLASS')]     = 'lujo_sedan'    # Sedán mediano premium
etiquetas[('MERCEDES-BENZ', 'R-CLASS')]     = 'lujo_suv'      # Wagon grande premium AWD
etiquetas[('MERCEDES-BENZ', 'SLC-CLASS')]   = 'deportivo'     # Roadster compacto premium
etiquetas[('MERCEDES-BENZ', 'SLK-CLASS')]   = 'deportivo'     # Roadster compacto premium
etiquetas[('MERCEDES-BENZ', 'M-CLASS')]     = 'lujo_suv'      # SUV mediano premium
etiquetas[('MERCEDES-BENZ', 'E-CLASS')]     = 'lujo_sedan'    # Sedán ejecutivo premium
etiquetas[('MERCEDES-BENZ', 'CLK-CLASS')]   = 'deportivo'     # Coupe/conv premium
etiquetas[('MERCEDES-BENZ', 'GLE-CLASS')]   = 'lujo_suv'      # SUV grande premium
etiquetas[('MERCEDES-BENZ', 'CLS-CLASS')]   = 'lujo_sedan'    # Fastback ejecutivo premium
etiquetas[('MERCEDES-BENZ', 'GL-CLASS')]    = 'lujo_suv'      # SUV grande premium 7 plazas
etiquetas[('MERCEDES-BENZ', 'GLE-CLASS COUPE')]= 'lujo_suv'   # SUV coupe performance
etiquetas[('MERCEDES-BENZ', 'GLS-CLASS')]   = 'lujo_suv'      # SUV grande premium 7 plazas
etiquetas[('MERCEDES-BENZ', 'AMG GT')]      = 'hiper_lujo'    # Superdeportivo $124k
etiquetas[('MERCEDES-BENZ', 'SL-CLASS')]    = 'hiper_lujo'    # Roadster flagship $140k
etiquetas[('MERCEDES-BENZ', 'G-CLASS')]     = 'hiper_lujo'    # SUV iconic $146k off-road lujo
etiquetas[('MERCEDES-BENZ', 'S-CLASS')]     = 'hiper_lujo'    # Flagship sedán $157k
etiquetas[('MERCEDES-BENZ', 'CL-CLASS')]    = 'hiper_lujo'    # Coupe flagship $160k
etiquetas[('MERCEDES-BENZ', 'SLS AMG')]     = 'hiper_lujo'    # Gullwing $190k
etiquetas[('MERCEDES-BENZ', 'MAYBACH')]     = 'hiper_lujo'    # Ultra flagship $190k
etiquetas[('MERCEDES-BENZ', 'SLS AMG GT')]  = 'hiper_lujo'    # SLS GT $218k
etiquetas[('MERCEDES-BENZ', 'SLS AMG GT FINAL EDITION')]= 'hiper_lujo' # Edición final
etiquetas[('MERCEDES-BENZ', 'SLR MCLAREN')] = 'hiper_lujo'   # Superdeportivo $490k

# ── MITSUBISHI ────────────────────────────────────────────────────
etiquetas[('MITSUBISHI', 'EXPO')]            = 'compacto_urbano'  # Hatchback compacto
etiquetas[('MITSUBISHI', 'MIGHTY MAX PICKUP')]= 'aventura_pickup' # Pickup compacto
etiquetas[('MITSUBISHI', 'SIGMA')]           = 'sedan_familiar'   # Sedán mediano
etiquetas[('MITSUBISHI', 'PRECIS')]          = 'compacto_urbano'  # Subcompacto básico
etiquetas[('MITSUBISHI', 'VANWAGON')]        = 'sedan_familiar'   # Van familiar
etiquetas[('MITSUBISHI', '3000GT')]          = 'deportivo'        # Coupe deportivo turbo AWD
etiquetas[('MITSUBISHI', 'MIRAGE')]          = 'compacto_urbano'  # Subcompacto económico
etiquetas[('MITSUBISHI', 'MIRAGE G4')]       = 'compacto_urbano'  # Sedán subcompacto
etiquetas[('MITSUBISHI', 'LANCER SPORTBACK')]= 'compacto_urbano'  # Hatchback compacto
etiquetas[('MITSUBISHI', 'LANCER')]          = 'compacto_urbano'  # Sedán compacto
etiquetas[('MITSUBISHI', 'GALANT')]          = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('MITSUBISHI', 'I-MIEV')]          = 'compacto_urbano'  # Eléctrico micro urbano
etiquetas[('MITSUBISHI', 'OUTLANDER SPORT')] = 'suv_familiar'     # SUV compacto
etiquetas[('MITSUBISHI', 'ECLIPSE')]         = 'deportivo'        # Coupe deportivo FWD
etiquetas[('MITSUBISHI', 'RAIDER')]          = 'aventura_pickup'  # Pickup mediano
etiquetas[('MITSUBISHI', 'OUTLANDER')]       = 'suv_familiar'     # SUV mediano familiar
etiquetas[('MITSUBISHI', 'DIAMANTE')]        = 'lujo_sedan'       # Sedán grande premium
etiquetas[('MITSUBISHI', 'MONTERO SPORT')]   = 'suv_familiar'     # SUV mediano 4WD
etiquetas[('MITSUBISHI', 'ENDEAVOR')]        = 'suv_familiar'     # SUV mediano familiar
etiquetas[('MITSUBISHI', 'ECLIPSE SPYDER')]  = 'deportivo'        # Convertible deportivo
etiquetas[('MITSUBISHI', 'MONTERO')]         = 'aventura_pickup'  # SUV 4WD off-road
etiquetas[('MITSUBISHI', 'LANCER EVOLUTION')]= 'deportivo'        # Sedán rally AWD turbo icónico

# ── NISSAN ────────────────────────────────────────────────────────
etiquetas[('NISSAN', 'AXXESS')]          = 'sedan_familiar'   # Minivan familiar
etiquetas[('NISSAN', 'VAN')]             = 'sedan_familiar'   # Van de pasajeros
etiquetas[('NISSAN', 'PULSAR')]          = 'compacto_urbano'  # Coupe compacto básico
etiquetas[('NISSAN', 'NX')]              = 'compacto_urbano'  # Coupe compacto
etiquetas[('NISSAN', 'STANZA')]          = 'compacto_urbano'  # Sedán compacto
etiquetas[('NISSAN', '200SX')]           = 'deportivo'        # Coupe compacto deportivo
etiquetas[('NISSAN', 'TRUCK')]           = 'aventura_pickup'  # Pickup compacto
etiquetas[('NISSAN', '300ZX')]           = 'deportivo'        # Coupe deportivo RWD turbo
etiquetas[('NISSAN', '240SX')]           = 'deportivo'        # Coupe RWD icónico drift
etiquetas[('NISSAN', 'VERSA')]           = 'compacto_urbano'  # Subcompacto urbano
etiquetas[('NISSAN', 'VERSA NOTE')]      = 'compacto_urbano'  # Hatchback subcompacto
etiquetas[('NISSAN', 'CUBE')]            = 'compacto_urbano'  # Wagon compacto urbano
etiquetas[('NISSAN', 'SENTRA')]          = 'compacto_urbano'  # Sedán compacto popular
etiquetas[('NISSAN', 'ROGUE SELECT')]    = 'suv_familiar'     # SUV compacto familiar
etiquetas[('NISSAN', 'NV200')]           = 'sedan_familiar'   # Van compacta comercial
etiquetas[('NISSAN', 'JUKE')]            = 'suv_familiar'     # SUV compacto urbano peculiar
etiquetas[('NISSAN', 'ROGUE')]           = 'suv_familiar'     # SUV compacto popular
etiquetas[('NISSAN', 'ALTIMA HYBRID')]   = 'sedan_familiar'   # Sedán híbrido familiar
etiquetas[('NISSAN', 'ALTIMA')]          = 'sedan_familiar'   # Sedán mediano popular
etiquetas[('NISSAN', 'XTERRA')]          = 'aventura_pickup'  # SUV mediano 4WD off-road
etiquetas[('NISSAN', 'FRONTIER')]        = 'aventura_pickup'  # Pickup mediano 4WD
etiquetas[('NISSAN', 'QUEST')]           = 'sedan_familiar'   # Minivan familiar
etiquetas[('NISSAN', 'PATHFINDER')]      = 'suv_familiar'     # SUV grande familiar
etiquetas[('NISSAN', 'MAXIMA')]          = 'sedan_familiar'   # Sedán grande deportivo FWD
etiquetas[('NISSAN', 'MURANO')]          = 'suv_familiar'     # SUV mediano popular
etiquetas[('NISSAN', '350Z')]            = 'deportivo'        # Roadster/coupe deportivo RWD
etiquetas[('NISSAN', 'TITAN')]           = 'aventura_pickup'  # Pickup grande 4WD
etiquetas[('NISSAN', '370Z')]            = 'deportivo'        # Coupe deportivo RWD
etiquetas[('NISSAN', 'MURANO CROSSCABRIOLET')]= 'deportivo'   # SUV convertible único
etiquetas[('NISSAN', 'ARMADA')]          = 'aventura_pickup'  # SUV grande 4WD
etiquetas[('NISSAN', 'GT-R')]            = 'deportivo'        # Superdeportivo AWD $119k — no hiper_lujo, es accesible en ese mundo

# ── OLDSMOBILE ────────────────────────────────────────────────────
etiquetas[('OLDSMOBILE', 'ACHIEVA')]         = 'compacto_urbano'  # Sedán compacto
etiquetas[('OLDSMOBILE', 'CUTLASS CALAIS')]  = 'compacto_urbano'  # Coupe compacto
etiquetas[('OLDSMOBILE', 'CUSTOM CRUISER')]  = 'sedan_familiar'   # Wagon grande familiar
etiquetas[('OLDSMOBILE', 'CIERA')]           = 'sedan_familiar'   # Wagon mediano familiar
etiquetas[('OLDSMOBILE', 'NINETY-EIGHT')]    = 'lujo_sedan'       # Sedán grande premium
etiquetas[('OLDSMOBILE', 'EIGHTY-EIGHT ROYALE')]= 'sedan_familiar' # Sedán grande
etiquetas[('OLDSMOBILE', 'CUTLASS SUPREME')] = 'sedan_familiar'   # Coupe mediano
etiquetas[('OLDSMOBILE', 'CUTLASS CIERA')]   = 'sedan_familiar'   # Sedán mediano
etiquetas[('OLDSMOBILE', 'TORONADO')]        = 'deportivo'        # Coupe grande FWD lujo/deportivo
etiquetas[('OLDSMOBILE', 'REGENCY')]         = 'lujo_sedan'       # Sedán grande premium
etiquetas[('OLDSMOBILE', 'CUTLASS')]         = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('OLDSMOBILE', 'EIGHTY-EIGHT')]    = 'sedan_familiar'   # Sedán grande familiar
etiquetas[('OLDSMOBILE', 'LSS')]             = 'lujo_sedan'       # Sedán grande premium
etiquetas[('OLDSMOBILE', 'INTRIGUE')]        = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('OLDSMOBILE', 'ALERO')]           = 'compacto_urbano'  # Coupe/sedán compacto
etiquetas[('OLDSMOBILE', 'SILHOUETTE')]      = 'sedan_familiar'   # Minivan familiar
etiquetas[('OLDSMOBILE', 'AURORA')]          = 'lujo_sedan'       # Sedán grande premium
etiquetas[('OLDSMOBILE', 'BRAVADA')]         = 'suv_familiar'     # SUV mediano AWD

# ── PLYMOUTH ──────────────────────────────────────────────────────
etiquetas[('PLYMOUTH', 'ACCLAIM')]       = 'compacto_urbano'  # Sedán compacto básico
etiquetas[('PLYMOUTH', 'BREEZE')]        = 'compacto_urbano'  # Sedán compacto
etiquetas[('PLYMOUTH', 'COLT')]          = 'compacto_urbano'  # Wagon compacto
etiquetas[('PLYMOUTH', 'HORIZON')]       = 'compacto_urbano'  # Hatchback básico
etiquetas[('PLYMOUTH', 'LASER')]         = 'deportivo'        # Hatchback deportivo turbo
etiquetas[('PLYMOUTH', 'SUNDANCE')]      = 'compacto_urbano'  # Hatchback compacto
etiquetas[('PLYMOUTH', 'VOYAGER')]       = 'sedan_familiar'   # Minivan familiar
etiquetas[('PLYMOUTH', 'GRAND VOYAGER')] = 'sedan_familiar'   # Minivan grande familiar
etiquetas[('PLYMOUTH', 'NEON')]          = 'compacto_urbano'  # Sedán compacto accesible
etiquetas[('PLYMOUTH', 'PROWLER')]       = 'deportivo'        # Roadster retro deportivo

# ── PONTIAC ───────────────────────────────────────────────────────
etiquetas[('PONTIAC', '6000')]           = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('PONTIAC', 'LE MANS')]        = 'compacto_urbano'  # Coupe compacto básico
etiquetas[('PONTIAC', 'SUNBIRD')]        = 'compacto_urbano'  # Coupe compacto
etiquetas[('PONTIAC', 'TRANS SPORT')]    = 'sedan_familiar'   # Minivan familiar
etiquetas[('PONTIAC', 'SUNFIRE')]        = 'compacto_urbano'  # Coupe compacto
etiquetas[('PONTIAC', 'G3')]             = 'compacto_urbano'  # Hatchback subcompacto
etiquetas[('PONTIAC', 'G5')]             = 'compacto_urbano'  # Coupe compacto
etiquetas[('PONTIAC', 'VIBE')]           = 'compacto_urbano'  # Hatchback compacto practico
etiquetas[('PONTIAC', 'FIREBIRD')]       = 'deportivo'        # Muscle car pony icónico
etiquetas[('PONTIAC', 'GRAND AM')]       = 'compacto_urbano'  # Sedán/coupe compacto
etiquetas[('PONTIAC', 'AZTEK')]          = 'suv_familiar'     # SUV mediano crossover
etiquetas[('PONTIAC', 'GRAND PRIX')]     = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('PONTIAC', 'G6')]             = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('PONTIAC', 'MONTANA SV6')]    = 'sedan_familiar'   # Minivan familiar AWD
etiquetas[('PONTIAC', 'TORRENT')]        = 'suv_familiar'     # SUV compacto AWD
etiquetas[('PONTIAC', 'SOLSTICE')]       = 'deportivo'        # Roadster deportivo RWD
etiquetas[('PONTIAC', 'MONTANA')]        = 'sedan_familiar'   # Minivan familiar
etiquetas[('PONTIAC', 'BONNEVILLE')]     = 'sedan_familiar'   # Sedán grande familiar
etiquetas[('PONTIAC', 'G8')]             = 'deportivo'        # Sedán australiano RWD performance
etiquetas[('PONTIAC', 'GTO')]            = 'deportivo'        # Muscle car coupe RWD

# ── PORSCHE ───────────────────────────────────────────────────────
etiquetas[('PORSCHE', '944')]            = 'deportivo'        # Coupe deportivo RWD clásico
etiquetas[('PORSCHE', '968')]            = 'deportivo'        # Convertible deportivo RWD
etiquetas[('PORSCHE', '928')]            = 'deportivo'        # Coupe GT premium
etiquetas[('PORSCHE', 'CAYMAN S')]       = 'deportivo'        # Coupe mid-engine RWD
etiquetas[('PORSCHE', '718 CAYMAN')]     = 'deportivo'        # Coupe mid-engine moderno
etiquetas[('PORSCHE', 'BOXSTER')]        = 'deportivo'        # Roadster mid-engine RWD
etiquetas[('PORSCHE', 'MACAN')]          = 'lujo_suv'         # SUV compacto performance
etiquetas[('PORSCHE', 'CAYMAN')]         = 'deportivo'        # Coupe mid-engine RWD
etiquetas[('PORSCHE', 'CAYENNE')]        = 'lujo_suv'         # SUV mediano performance premium
etiquetas[('PORSCHE', 'PANAMERA')]       = 'hiper_lujo'       # Sedán gran turismo $123k
etiquetas[('PORSCHE', '911')]            = 'hiper_lujo'       # Icono $124k+ superdeportivo
etiquetas[('PORSCHE', 'CARRERA GT')]     = 'hiper_lujo'       # Superdeportivo $440k

# ── ROLLS-ROYCE ───────────────────────────────────────────────────
for model in ['SILVER SERAPH','PARK WARD','GHOST','WRAITH','GHOST SERIES II',
              'DAWN','CORNICHE','PHANTOM COUPE','PHANTOM','PHANTOM DROPHEAD COUPE']:
    etiquetas[('ROLLS-ROYCE', model)] = 'hiper_lujo'

# ── SAAB ──────────────────────────────────────────────────────────
etiquetas[('SAAB', '900')]               = 'compacto_urbano'  # Hatchback compacto europeo
etiquetas[('SAAB', '9000')]              = 'sedan_familiar'   # Hatchback mediano
etiquetas[('SAAB', '9-2X')]              = 'deportivo'        # Wagon AWD basado en Impreza WRX
etiquetas[('SAAB', '9-3 GRIFFIN')]       = 'lujo_sedan'       # Sedán compacto premium
etiquetas[('SAAB', '09-mar')]            = 'lujo_sedan'       # Sedán compacto premium
etiquetas[('SAAB', '9-4X')]              = 'lujo_suv'         # SUV mediano premium
etiquetas[('SAAB', '09-may')]            = 'lujo_sedan'       # Sedán mediano premium
etiquetas[('SAAB', '9-7X')]              = 'lujo_suv'         # SUV mediano premium

# ── SCION ─────────────────────────────────────────────────────────
etiquetas[('SCION', 'XA')]               = 'compacto_urbano'  # Hatchback subcompacto
etiquetas[('SCION', 'IQ')]               = 'compacto_urbano'  # Micro urbano
etiquetas[('SCION', 'IA')]               = 'compacto_urbano'  # Sedán subcompacto
etiquetas[('SCION', 'XD')]               = 'compacto_urbano'  # Hatchback compacto
etiquetas[('SCION', 'XB')]               = 'compacto_urbano'  # Wagon compacto urbano caja
etiquetas[('SCION', 'IM')]               = 'compacto_urbano'  # Hatchback compacto
etiquetas[('SCION', 'TC')]               = 'deportivo'        # Coupe compacto deportivo
etiquetas[('SCION', 'FR-S')]             = 'deportivo'        # Coupe RWD deportivo puro

# ── SPYKER ────────────────────────────────────────────────────────
etiquetas[('SPYKER', 'C8')]              = 'hiper_lujo'       # Superdeportivo holandés $213k

# ── SUBARU ────────────────────────────────────────────────────────
etiquetas[('SUBARU', 'JUSTY')]           = 'compacto_urbano'  # Micro urbano básico
etiquetas[('SUBARU', 'LOYALE')]          = 'compacto_urbano'  # Wagon compacto 4WD
etiquetas[('SUBARU', 'XT')]              = 'deportivo'        # Coupe deportivo aerodinámico
etiquetas[('SUBARU', 'SVX')]             = 'deportivo'        # Coupe GT AWD
etiquetas[('SUBARU', 'IMPREZA')]         = 'compacto_urbano'  # Hatchback compacto AWD
etiquetas[('SUBARU', 'CROSSTREK')]       = 'suv_familiar'     # Crossover compacto AWD
etiquetas[('SUBARU', 'XV CROSSTREK')]    = 'suv_familiar'     # Crossover compacto AWD
etiquetas[('SUBARU', 'BAJA')]            = 'aventura_pickup'  # Pickup AWD peculiar
etiquetas[('SUBARU', 'LEGACY')]          = 'sedan_familiar'   # Sedán AWD familiar
etiquetas[('SUBARU', 'FORESTER')]        = 'suv_familiar'     # SUV compacto AWD popular
etiquetas[('SUBARU', 'BRZ')]             = 'deportivo'        # Coupe RWD deportivo puro
etiquetas[('SUBARU', 'OUTBACK')]         = 'suv_familiar'     # Wagon AWD aventurero popular
etiquetas[('SUBARU', 'IMPREZA WRX')]     = 'deportivo'        # Sedán turbo AWD performance
etiquetas[('SUBARU', 'WRX')]             = 'deportivo'        # Sedán turbo AWD performance
etiquetas[('SUBARU', 'TRIBECA')]         = 'suv_familiar'     # SUV mediano AWD
etiquetas[('SUBARU', 'B9 TRIBECA')]      = 'suv_familiar'     # SUV mediano AWD

# ── SUZUKI ────────────────────────────────────────────────────────
etiquetas[('SUZUKI', 'SAMURAI')]         = 'aventura_pickup'  # SUV 4WD convertible off-road
etiquetas[('SUZUKI', 'X-90')]            = 'aventura_pickup'  # Mini SUV 4WD
etiquetas[('SUZUKI', 'SIDEKICK')]        = 'suv_familiar'     # SUV compacto 4WD
etiquetas[('SUZUKI', 'SWIFT')]           = 'compacto_urbano'  # Subcompacto urbano
etiquetas[('SUZUKI', 'ESTEEM')]          = 'compacto_urbano'  # Wagon compacto accesible
etiquetas[('SUZUKI', 'RENO')]            = 'compacto_urbano'  # Hatchback compacto
etiquetas[('SUZUKI', 'FORENZA')]         = 'compacto_urbano'  # Sedán compacto
etiquetas[('SUZUKI', 'AERIO')]           = 'compacto_urbano'  # Sedán/wagon compacto
etiquetas[('SUZUKI', 'VITARA')]          = 'suv_familiar'     # SUV compacto 4WD
etiquetas[('SUZUKI', 'SX4')]             = 'compacto_urbano'  # Hatchback compacto AWD
etiquetas[('SUZUKI', 'VERONA')]          = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('SUZUKI', 'GRAND VITARA')]    = 'suv_familiar'     # SUV mediano RWD
etiquetas[('SUZUKI', 'XL-7')]            = 'suv_familiar'     # SUV mediano familiar
etiquetas[('SUZUKI', 'KIZASHI')]         = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('SUZUKI', 'EQUATOR')]         = 'aventura_pickup'  # Pickup compacto RWD
etiquetas[('SUZUKI', 'XL7')]             = 'suv_familiar'     # SUV mediano familiar

# ── TOYOTA ────────────────────────────────────────────────────────
etiquetas[('TOYOTA', 'CRESSIDA')]        = 'lujo_sedan'       # Sedán mediano premium RWD 90s
etiquetas[('TOYOTA', 'TERCEL')]          = 'compacto_urbano'  # Coupe subcompacto básico
etiquetas[('TOYOTA', 'PASEO')]           = 'compacto_urbano'  # Coupe compacto
etiquetas[('TOYOTA', 'MR2')]             = 'deportivo'        # Mid-engine deportivo RWD icónico
etiquetas[('TOYOTA', 'PREVIA')]          = 'sedan_familiar'   # Minivan familiar AWD
etiquetas[('TOYOTA', 'PICKUP')]          = 'aventura_pickup'  # Pickup compacto clásico 4WD
etiquetas[('TOYOTA', 'T100')]            = 'aventura_pickup'  # Pickup mediano
etiquetas[('TOYOTA', 'ECHO')]            = 'compacto_urbano'  # Subcompacto económico
etiquetas[('TOYOTA', 'YARIS')]           = 'compacto_urbano'  # Subcompacto urbano
etiquetas[('TOYOTA', 'YARIS IA')]        = 'compacto_urbano'  # Sedán subcompacto
etiquetas[('TOYOTA', 'COROLLA IM')]      = 'compacto_urbano'  # Hatchback compacto
etiquetas[('TOYOTA', 'SUPRA')]           = 'deportivo'        # Coupe deportivo RWD turbo icónico
etiquetas[('TOYOTA', 'COROLLA')]         = 'compacto_urbano'  # Sedán compacto más vendido mundo
etiquetas[('TOYOTA', 'MATRIX')]          = 'compacto_urbano'  # Hatchback compacto práctico
etiquetas[('TOYOTA', 'CELICA')]          = 'deportivo'        # Coupe deportivo FWD clásico
etiquetas[('TOYOTA', 'PRIUS C')]         = 'compacto_urbano'  # Híbrido subcompacto urbano
etiquetas[('TOYOTA', 'CAMRY SOLARA')]    = 'sedan_familiar'   # Coupe/convertible mediano
etiquetas[('TOYOTA', 'MR2 SPYDER')]      = 'deportivo'        # Roadster mid-engine RWD
etiquetas[('TOYOTA', '86')]              = 'deportivo'        # Coupe RWD deportivo puro
etiquetas[('TOYOTA', 'PRIUS')]           = 'compacto_urbano'  # Híbrido icónico urbano
etiquetas[('TOYOTA', 'CAMRY')]           = 'sedan_familiar'   # Sedán mediano más vendido
etiquetas[('TOYOTA', 'FJ CRUISER')]      = 'aventura_pickup'  # SUV 4WD off-road retro
etiquetas[('TOYOTA', 'CAMRY HYBRID')]    = 'sedan_familiar'   # Sedán híbrido familiar
etiquetas[('TOYOTA', 'RAV4')]            = 'suv_familiar'     # SUV compacto popular
etiquetas[('TOYOTA', 'PRIUS V')]         = 'sedan_familiar'   # Hybrid wagon familiar
etiquetas[('TOYOTA', 'PRIUS PRIME')]     = 'compacto_urbano'  # Híbrido enchufable compacto
etiquetas[('TOYOTA', 'TACOMA')]          = 'aventura_pickup'  # Pickup mediano 4WD muy popular
etiquetas[('TOYOTA', 'RAV4 HYBRID')]     = 'suv_familiar'     # SUV compacto híbrido
etiquetas[('TOYOTA', 'VENZA')]           = 'suv_familiar'     # Crossover wagon mediano
etiquetas[('TOYOTA', 'AVALON')]          = 'lujo_sedan'       # Sedán grande premium FWD
etiquetas[('TOYOTA', 'HIGHLANDER')]      = 'suv_familiar'     # SUV mediano 3 filas familiar
etiquetas[('TOYOTA', 'SIENNA')]          = 'sedan_familiar'   # Minivan familiar referente
etiquetas[('TOYOTA', 'TUNDRA')]          = 'aventura_pickup'  # Pickup grande 4WD
etiquetas[('TOYOTA', '4RUNNER')]         = 'aventura_pickup'  # SUV 4WD off-road clásico
etiquetas[('TOYOTA', 'AVALON HYBRID')]   = 'lujo_sedan'       # Sedán grande híbrido premium
etiquetas[('TOYOTA', 'HIGHLANDER HYBRID')]= 'suv_familiar'    # SUV grande híbrido familiar
etiquetas[('TOYOTA', 'RAV4 EV')]         = 'suv_familiar'     # SUV compacto eléctrico
etiquetas[('TOYOTA', 'SEQUOIA')]         = 'aventura_pickup'  # SUV grande 4WD
etiquetas[('TOYOTA', 'LAND CRUISER')]    = 'hiper_lujo'       # SUV 4WD flagship $83k — icono off-road lujo

# ── VOLKSWAGEN ────────────────────────────────────────────────────
etiquetas[('VOLKSWAGEN', 'CABRIOLET')]       = 'deportivo'        # Convertible compacto
etiquetas[('VOLKSWAGEN', 'CORRADO')]         = 'deportivo'        # Coupe deportivo VR6
etiquetas[('VOLKSWAGEN', 'FOX')]             = 'compacto_urbano'  # Coupe subcompacto básico
etiquetas[('VOLKSWAGEN', 'VANAGON')]         = 'sedan_familiar'   # Van clásica familiar
etiquetas[('VOLKSWAGEN', 'RABBIT')]          = 'compacto_urbano'  # Hatchback compacto clásico
etiquetas[('VOLKSWAGEN', 'CABRIO')]          = 'deportivo'        # Convertible compacto
etiquetas[('VOLKSWAGEN', 'NEW BEETLE')]      = 'compacto_urbano'  # Hatchback retro compacto
etiquetas[('VOLKSWAGEN', 'GOLF')]            = 'compacto_urbano'  # Hatchback compacto referente
etiquetas[('VOLKSWAGEN', 'JETTA')]           = 'compacto_urbano'  # Sedán compacto popular
etiquetas[('VOLKSWAGEN', 'JETTA SPORTWAGEN')]= 'compacto_urbano'  # Wagon compacto
etiquetas[('VOLKSWAGEN', 'GLI')]             = 'deportivo'        # Jetta performance
etiquetas[('VOLKSWAGEN', 'BEETLE')]          = 'compacto_urbano'  # Hatchback retro moderno
etiquetas[('VOLKSWAGEN', 'GOLF SPORTWAGEN')] = 'compacto_urbano'  # Wagon compacto
etiquetas[('VOLKSWAGEN', 'EUROVAN')]         = 'sedan_familiar'   # Van grande familiar
etiquetas[('VOLKSWAGEN', 'JETTA GLI')]       = 'deportivo'        # Jetta performance
etiquetas[('VOLKSWAGEN', 'PASSAT')]          = 'sedan_familiar'   # Sedán mediano familiar
etiquetas[('VOLKSWAGEN', 'GTI')]             = 'deportivo'        # Hot hatch icónico
etiquetas[('VOLKSWAGEN', 'JETTA HYBRID')]    = 'compacto_urbano'  # Sedán híbrido compacto
etiquetas[('VOLKSWAGEN', 'GOLF GTI')]        = 'deportivo'        # Hot hatch performance
etiquetas[('VOLKSWAGEN', 'GOLF ALLTRACK')]   = 'suv_familiar'     # Wagon AWD crossover
etiquetas[('VOLKSWAGEN', 'BEETLE CONVERTIBLE')]= 'deportivo'      # Convertible retro
etiquetas[('VOLKSWAGEN', 'R32')]             = 'deportivo'        # Golf VR6 AWD performance
etiquetas[('VOLKSWAGEN', 'TIGUAN')]          = 'suv_familiar'     # SUV compacto familiar
etiquetas[('VOLKSWAGEN', 'E-GOLF')]          = 'compacto_urbano'  # Golf eléctrico urbano
etiquetas[('VOLKSWAGEN', 'ROUTAN')]          = 'sedan_familiar'   # Minivan familiar
etiquetas[('VOLKSWAGEN', 'CC')]              = 'lujo_sedan'       # Fastback premium mediano
etiquetas[('VOLKSWAGEN', 'GOLF R')]          = 'deportivo'        # Golf AWD máximo performance
etiquetas[('VOLKSWAGEN', 'EOS')]             = 'deportivo'        # Convertible techo rígido
etiquetas[('VOLKSWAGEN', 'TOUAREG 2')]       = 'lujo_suv'         # SUV mediano premium AWD
etiquetas[('VOLKSWAGEN', 'TOUAREG')]         = 'lujo_suv'         # SUV mediano premium AWD
etiquetas[('VOLKSWAGEN', 'PHAETON')]         = 'hiper_lujo'       # Sedán flagship $83k ultra premium

# ── VOLVO ─────────────────────────────────────────────────────────
etiquetas[('VOLVO', '240')]              = 'sedan_familiar'   # Sedán/wagon clásico seguro
etiquetas[('VOLVO', '740')]              = 'sedan_familiar'   # Wagon mediano familiar
etiquetas[('VOLVO', '760')]              = 'lujo_sedan'       # Sedán mediano premium
etiquetas[('VOLVO', '780')]              = 'lujo_sedan'       # Coupe premium
etiquetas[('VOLVO', '940')]              = 'sedan_familiar'   # Sedán/wagon familiar
etiquetas[('VOLVO', '960')]              = 'lujo_sedan'       # Sedán mediano premium
etiquetas[('VOLVO', 'COUPE')]            = 'lujo_sedan'       # Coupe premium
etiquetas[('VOLVO', '850')]              = 'sedan_familiar'   # Sedán mediano familiar/deportivo
etiquetas[('VOLVO', 'V90')]              = 'lujo_sedan'       # Wagon premium moderno
etiquetas[('VOLVO', 'S70')]              = 'lujo_sedan'       # Sedán mediano premium
etiquetas[('VOLVO', 'C30')]              = 'deportivo'        # Hatchback compacto deportivo
etiquetas[('VOLVO', 'V40')]              = 'lujo_sedan'       # Wagon compacto premium
etiquetas[('VOLVO', 'S40')]              = 'lujo_sedan'       # Sedán compacto premium
etiquetas[('VOLVO', 'V50')]              = 'lujo_sedan'       # Wagon compacto premium
etiquetas[('VOLVO', 'V70')]              = 'lujo_sedan'       # Wagon mediano premium
etiquetas[('VOLVO', 'XC')]               = 'lujo_suv'         # SUV wagon premium AWD
etiquetas[('VOLVO', 'C70')]              = 'deportivo'        # Convertible premium
etiquetas[('VOLVO', 'S60')]              = 'lujo_sedan'       # Sedán mediano premium AWD
etiquetas[('VOLVO', 'XC70')]             = 'lujo_sedan'       # Wagon AWD premium
etiquetas[('VOLVO', 'S90')]              = 'lujo_sedan'       # Sedán grande premium AWD
etiquetas[('VOLVO', 'V60')]              = 'lujo_sedan'       # Wagon mediano premium AWD
etiquetas[('VOLVO', 'V60 CROSS COUNTRY')]= 'lujo_sedan'       # Wagon AWD premium aventurero
etiquetas[('VOLVO', 'S80')]              = 'lujo_sedan'       # Sedán grande premium
etiquetas[('VOLVO', 'XC60')]             = 'lujo_suv'         # SUV mediano premium AWD
etiquetas[('VOLVO', 'S60 CROSS COUNTRY')]= 'lujo_sedan'       # Sedán AWD premium
etiquetas[('VOLVO', 'XC90')]             = 'lujo_suv'         # SUV grande premium 7 plazas

# ── Aplicar etiquetas al dataframe ────────────────────────────────
df['perfil'] = df.apply(lambda r: etiquetas.get((r['Make'], r['Model']), None), axis=1)

# Verificar cobertura
sin_etiqueta = df[df['perfil'].isna()]
print(f"Total etiquetados: {df['perfil'].notna().sum()} / {len(df)}")
print(f"Sin etiqueta: {len(sin_etiqueta)}")
if len(sin_etiqueta) > 0:
    print(sin_etiqueta[['Make','Model']].to_string())

print(f"\nDistribución de perfiles:")
print(df['perfil'].value_counts())

df.to_csv('dataEPrueba.csv', index=False)
print("\n✅ Guardado: dataset_etiquetado_manual.csv")