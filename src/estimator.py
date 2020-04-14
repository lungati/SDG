def get_infections_by_requested_time(currently_infected, days):
    return currently_infected * (2 ** (days // 3))


def estimator(data, requested_time):
    impact = severe_impact = dict()
    impact["currentlyInfected"] = data["reportedCases"] * 10
    severe_impact["currentlyInfected"] = data["reportedCases"] * 50
    impact["infectionsByRequestedTime"] = get_infections_by_requested_time(
        impact["currentlyInfected"], requested_time)
    severe_impact["infectionsByRequestedTime"] = \
        get_infections_by_requested_time(
        severe_impact["currentlyInfected"], requested_time)
    impact["severeCasesByRequestedTime"] = int(
        0.15 * impact["infectionsByRequestedTime"]
    )
    severe_impact["severeCasesByRequestedTime"] = int(
        0.15 * severe_impact["infectionsByRequestedTime"]
    )
    impact["hospitalBedsByRequestedTime"] = int(
        0.35 * impact["severeCasesByRequestedTime"]
    )
    severe_impact["hospitalBedsByRequestedTime"] = int(
        0.35 * severe_impact["severeCasesByRequestedTime"]
    )
    impact["casesForICUByRequestedTime"] = int(
        0.05 * impact["infectionsByRequestedTime"]
    )
    severe_impact["casesForICUByRequestedTime"] = int(
        0.05 * severe_impact["infectionsByRequestedTime"]
    )
    impact["casesForVentilatorsByRequestedTime"] = int(
        0.02 * impact["infectionsByRequestedTime"]
    )
    severe_impact["casesForVentilatorsByRequestedTime"] = int(
        0.02 * severe_impact["infectionsByRequestedTime"]
    )
    impact["dollarsInFlight"] = (
        (impact["infectionsByRequestedTime"] * 0.65 * 1.5) / requested_time)
    severe_impact["dollarsInFlight"] = (
        (severe_impact["infectionsByRequestedTime"] * 0.65 * 1.5) /
        requested_time)
    return dict(data=data, impact=impact, severeImpact=severe_impact)
