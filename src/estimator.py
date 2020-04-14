def get_infections_by_requested_time(currently_infected, days):
    return currently_infected * (2 ** (days // 3))


def estimator(data, requested_time):
    impact = severe_impact = dict()
    impact["currentlyInfected"] = data["reportedCases"] * 10
    impact["infectionsByRequestedTime"] = get_infections_by_requested_time(
        impact["currentlyInfected"], requested_time)
    severe_impact["currentlyInfected"] = data["reportedCases"] * 50
    severe_impact["infectionsByRequestedTime"] = \
        get_infections_by_requested_time(
        severe_impact["currentlyInfected"], requested_time)
    import pdb; pdb.set_trace()
    return dict(data=data, impact=impact, severeImpact=severe_impact)
