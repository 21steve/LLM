risk_assessment_query_string='''query VesselsByIMOs($imo: String!) {
  vesselByIMO(imo: $imo) {
    id
    riskAssessment {
      complianceRisk {
        level
      }
      iuuFishingRisk {
        level
      }
      mavSCSRisk {
        level
        riskIndicators {
          name
        }
      }
      smugglingRisk {
        level
        indicators {
          risk
          name
          count
        }
      }
    }
    class
    flag
  }
}'''

def activities_input(includePropertyChanges:bool,limit:int,offset:int,from_date:str,to_date:str,vesselIdOrImo:str,coordinates:list[list]=None)->dict:
  # "polygon": {
  #     "type": "Polygon",
  #     "coordinates": [
  #       [
  #         [
  #           113.258057,
  #           19.823202
  #         ],
  #         [
  #           113.258057,
  #           23.007113
  #         ],
  #         [
  #           120.629883,
  #           23.007113
  #         ],
  #         [
  #           120.629883,
  #           19.823202
  #         ],
  #         [
  #           113.258057,
  #           19.823202
  #         ]
  #       ]
  #     ]
  #   }
  if coordinates:
    polygon={
        "type": "Polygon",
        "coordinates": [
          coordinates
        ]
      }
  else:
    polygon="null"
  
  return {
  "input": {
    "includePropertyChanges": includePropertyChanges,
    "limit": limit,
    "offset": offset,
    "timeRange": {
      "from": from_date,
      "to": to_date
    },
    "vesselIdOrImo": vesselIdOrImo,
    "types": [
      {
        "type": "MEETING"
        
      },
      {
        "type": "STANDING"
      },
      {
        "type": "LOW_SPEED_ANCHORED"
      },
      {
        "type": "LOW_SPEED_DRIFTING"
      },
      {
        "type": "LOW_SPEED_MOORED"
      },
      {
        "type": "LOW_SPEED_FISHING"
      },
      {
        "type": "LOW_SPEED_SERVICE"
      },
      {
        "type": "LOW_SPEED_RESEARCH"
      },
      {
        "type": "LOW_SPEED_OFFSHORE_FACILITY"
      },
      {
        "type": "LOW_SPEED_OTHER"
      },
      {
        "type": "MISSING"
      },
      
      {
        "type": "ID_MANIPULATION"
      },
      {
        "type": "PORT_CALL"
      },
      {
        "type": "DARK_ACTIVITY"
      },
      {
        "type": "MMSI_CHANGE"
      },
      {
        "type": "DEVIATION_FROM_PATTERN_FIRST_IN_POLYGON"
      },
      {
        "type": "COURSE_DEVIATION"
      },
      {
        "type": "ACCIDENT"
      },
      {
        "type": "DESTINATION_CHANGE"
      },
      {
        "type": "ETA_CHANGE"
      },
      {
        "type": "BAD_WEATHER"
      }
    ],
    "polygon": polygon,
  }
}

activities_query_string='''query VesselTimeline($input: VesselTimelineInput!) {
  vesselTimeline(input: $input) {
    nodes {
      ... on Activity {
        duration
        vesselId
        previousPortId
        startDate
        type
        startCoordinate
        endCoordinate
        nextPortId
        extraFields {
          ... on ExtraFields {
            activityType
          }
          ... on DarkActivityExtraFields {
            destinationChange
            draftChange
          }
          
          ... on DestinationChangeActivityExtraFields {
            newDestination
            oldDestination
          }
          ... on ETAChangeActivityExtraFields {
            newEta
            oldEta
          }
          ... on MeetingExtraFields {
            meetingType
          }
        }
      }
    }
    totalCount
  }
}'''