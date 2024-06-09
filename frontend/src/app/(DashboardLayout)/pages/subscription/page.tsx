'use client';
import Link from "next/link";
import {
  CardContent,
  Typography,
  Grid,
  Rating,
  Tooltip,
  Fab,
  Avatar,
  Box
} from "@mui/material";
import { Stack } from "@mui/system";
import { IconBasket } from "@tabler/icons-react";
import PageContainer from '@/app/(DashboardLayout)/components/container/PageContainer';
import DashboardCard from '@/app/(DashboardLayout)/components/shared/DashboardCard';
import BlankCard from "@/app/(DashboardLayout)/components/shared/BlankCard";

const myPlan = {
  title: "My Plan - Bronze",
  subheader: "Active",
  photo: '/images/plans/bronze.svg',
  price: 285,
  rating: 2,
  position: { right: -60, top: 60 },
};

const otherPlans = [
  {
    title: "Silver Plan",
    subheader: "Upgrade Available",
    photo: '/images/plans/silver.svg',
    price: 375,
    rating: 3,
    position: { top: 70, left: -60 },
  },
  {
    title: "Gold Plan",
    subheader: "Upgrade Available",
    photo: '/images/plans/gold.svg',
    price: 650,
    rating: 4,
    position: { top: -40, right: -50 },
  },
  {
    title: "Platinum Plan",
    subheader: "Upgrade Available",
    photo: '/images/plans/platinum.svg',
    price: 900,
    rating: 5,
    position: { top: -35, left: -70 },
  },
];

const SubscriptionPage = () => {
  return (
    <PageContainer title="Subscription Page" description="Manage your subscription plans">
      <DashboardCard title="My Plan">
        <Grid container spacing={3}>
          <Grid item xs={12} md={12}>
            <BlankCard>
              <Box
                sx={{
                  display: 'flex',
                  justifyContent: 'center',
                  alignItems: 'center',
                  height: 250,
                  position: 'relative',
                }}
              >
                <Avatar
                  src={myPlan.photo}
                  variant="square"
                  sx={{
                    height: '100%',
                    width: 'auto',
                    position: 'relative',
                    ...myPlan.position,
                  }}
                />
                <Tooltip title="Manage Plan">
                  <Fab
                    size="small"
                    color="primary"
                    sx={{ bottom: "75px", right: "15px", position: "absolute" }}
                  >
                    <IconBasket size="16" />
                  </Fab>
                </Tooltip>
              </Box>
              <CardContent sx={{ p: 3, pt: 2 }}>
                <Typography variant="h6">{myPlan.title}</Typography>
                <Stack
                  direction="row"
                  alignItems="center"
                  justifyContent="space-between"
                  mt={1}
                >
                  <Typography variant="h6">${myPlan.price}</Typography>
                  <Rating
                    name="read-only"
                    size="small"
                    value={myPlan.rating}
                    readOnly
                  />
                </Stack>
              </CardContent>
            </BlankCard>
          </Grid>
        </Grid>
      </DashboardCard>
      <DashboardCard title="Other Plans">
        <Grid container spacing={3}>
          {otherPlans.map((plan, index) => (
            <Grid item xs={12} md={4} lg={4} key={index}>
              <BlankCard>
                <Box
                  sx={{
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center',
                    height: 250,
                    position: 'relative',
                  }}
                >
                  <Avatar
                    src={plan.photo}
                    variant="square"
                    sx={{
                      height: '100%',
                      width: 'auto',
                      position: 'relative',
                      ...plan.position,
                    }}
                  />
                  <Tooltip title="Upgrade Plan">
                    <Fab
                      size="small"
                      color="primary"
                      sx={{ bottom: "75px", right: "15px", position: "absolute" }}
                    >
                      <IconBasket size="16" />
                    </Fab>
                  </Tooltip>
                </Box>
                <CardContent sx={{ p: 3, pt: 2 }}>
                  <Typography variant="h6">{plan.title}</Typography>
                  <Stack
                    direction="row"
                    alignItems="center"
                    justifyContent="space-between"
                    mt={1}
                  >
                    <Typography variant="h6">${plan.price}</Typography>
                    <Rating
                      name="read-only"
                      size="small"
                      value={plan.rating}
                      readOnly
                    />
                  </Stack>
                </CardContent>
              </BlankCard>
            </Grid>
          ))}
        </Grid>
      </DashboardCard>
    </PageContainer>
  );
};

export default SubscriptionPage;
