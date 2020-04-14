from collections import namedtuple


def get_infections_by_requested_time(currently_infected, days):
    return currently_infected * (2 ** (days // 3))


def estimator(data, requested_time):
    data = namedtuple(data)

    impact = severeImpact = namedtuple()
    impact.currentlyInfected = data.reportedCases * 10
    impact.infectionsByRequestedTime = get_infections_by_requested_time(
        impact.currentlyInfected, requested_time)
    severeImpact.currentlyInfected = data.reportedCases * 50
    severeImpact.infectionsByRequestedTime = get_infections_by_requested_time(
        severeImpact.currentlyInfected, requested_time)

    return dict(data=data, impact=impact, severeImpact=severeImpact)
